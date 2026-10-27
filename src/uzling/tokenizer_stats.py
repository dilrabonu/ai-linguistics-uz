"""Tokenizer fairness statistics: fertility, parity, and morphological alignment.

Definitions used everywhere in the book (§4):

* **word** -- a whitespace-separated chunk with surrounding punctuation and symbols
  (Unicode categories P* and S*) stripped; chunks that become empty (``—``, ``%``)
  are not words. The Uzbek marks ʻ and ʼ are letters (category Lm), so they are
  never stripped. See :func:`words`.
* **fertility** = total tokens / total words (corpus level; Rust et al., 2021).
  :func:`mean_sentence_fertility` gives the mean of per-sentence ratios.
* **parity** = tokens(target) / tokens(reference) on *parallel* text
  (Petrov et al., 2023). Corpus level: ratio of sums.
* **continued-word rate** = share of words split into more than one token.
* **characters / bytes per token** = corpus characters (UTF-8 bytes) / tokens.
* **context capacity** = words that fit into a window of N tokens = N / fertility.
* **boundary precision / recall / F1** = token boundaries vs gold morpheme
  boundaries inside a word, compared as byte offsets (micro-averaged).

Tokens are always counted with ``add_special_tokens=False`` (no BOS/EOS/CLS/SEP).
Whole sentences are tokenized for token counts; single words are tokenized as
``" " + word`` (the form a word has inside a sentence) for per-word statistics.

The module needs only ``numpy``. :class:`TokenizerAdapter` wraps any Hugging Face
tokenizer by duck typing, so ``transformers`` is not imported here.
"""

from __future__ import annotations

import re
import unicodedata
from collections.abc import Callable, Iterable, Sequence
from functools import lru_cache

import numpy as np

Tokenize = Callable[[str], Sequence]

# ---------------------------------------------------------------- words


def _is_punct_or_symbol(ch: str) -> bool:
    return unicodedata.category(ch)[0] in "PS"


def strip_punct(chunk: str) -> str:
    """Remove punctuation and symbols from both ends of ``chunk``.

    >>> strip_punct("«Toshkent»,"), strip_punct("togʻ"), strip_punct("—")
    ('Toshkent', 'togʻ', '')
    """
    start, end = 0, len(chunk)
    while start < end and _is_punct_or_symbol(chunk[start]):
        start += 1
    while end > start and _is_punct_or_symbol(chunk[end - 1]):
        end -= 1
    return chunk[start:end]


def words(text: str) -> list[str]:
    """Split ``text`` into words (the single word definition used in the book).

    >>> words("Oʻzbekiston — katta mamlakat (2024-yil).")
    ['Oʻzbekiston', 'katta', 'mamlakat', '2024-yil']
    """
    return [w for w in (strip_punct(c) for c in text.split()) if w]


def count_words(text: str) -> int:
    return len(words(text))


# ---------------------------------------------------------------- simple API


def count_tokens(tokenize: Tokenize, sentences: Sequence[str]) -> int:
    return sum(len(tokenize(s)) for s in sentences)


def fertility(tokenize: Tokenize, sentences: Sequence[str]) -> float:
    """Corpus-level tokens per word for any ``tokenize`` callable."""
    n_words = sum(count_words(s) for s in sentences)
    if n_words == 0:
        raise ValueError("no words in input")
    return count_tokens(tokenize, sentences) / n_words


def parity(tokenize: Tokenize, target: Sequence[str], reference: Sequence[str]) -> float:
    """Token-count ratio of ``target`` to its parallel ``reference`` (usually English).

    A parity of 2.0 means the same content costs twice as many tokens.
    """
    if len(target) != len(reference):
        raise ValueError("target and reference must be parallel (same length)")
    ref = count_tokens(tokenize, reference)
    if ref == 0:
        raise ValueError("reference has no tokens")
    return count_tokens(tokenize, target) / ref


# ---------------------------------------------------------------- statistics on counts


def corpus_fertility(n_tokens: Sequence[int], n_words: Sequence[int]) -> float:
    total_words = int(np.sum(n_words))
    if total_words == 0:
        raise ValueError("no words in input")
    return float(np.sum(n_tokens)) / total_words


def mean_sentence_fertility(n_tokens: Sequence[int], n_words: Sequence[int]) -> float:
    """Mean of per-sentence fertility; sentences without words are skipped."""
    t, w = np.asarray(n_tokens, float), np.asarray(n_words, float)
    mask = w > 0
    return float(np.mean(t[mask] / w[mask]))


def corpus_parity(tok_target: Sequence[int], tok_reference: Sequence[int]) -> float:
    if len(tok_target) != len(tok_reference):
        raise ValueError("target and reference must be parallel (same length)")
    ref = float(np.sum(tok_reference))
    if ref == 0:
        raise ValueError("reference has no tokens")
    return float(np.sum(tok_target)) / ref


def sentence_parities(tok_target: Sequence[int], tok_reference: Sequence[int]) -> np.ndarray:
    t, r = np.asarray(tok_target, float), np.asarray(tok_reference, float)
    if t.shape != r.shape:
        raise ValueError("target and reference must be parallel (same length)")
    if np.any(r == 0):
        raise ValueError("a reference sentence has no tokens")
    return t / r


def bootstrap_ci(
    stat: Callable[..., float],
    arrays: Sequence[Sequence[float]],
    n_boot: int = 1000,
    seed: int = 42,
    level: float = 0.95,
) -> tuple[float, float]:
    """Percentile bootstrap CI of ``stat(*arrays)``, resampling rows jointly.

    >>> lo, hi = bootstrap_ci(lambda a: float(np.mean(a)), [np.ones(50)])
    >>> (lo, hi)
    (1.0, 1.0)
    """
    arrs = [np.asarray(a) for a in arrays]
    n = len(arrs[0])
    if any(len(a) != n for a in arrs):
        raise ValueError("arrays must have the same length")
    rng = np.random.default_rng(seed)
    stats = np.empty(n_boot)
    for i in range(n_boot):
        idx = rng.integers(0, n, n)
        stats[i] = stat(*(a[idx] for a in arrs))
    alpha = (1 - level) / 2
    lo, hi = np.quantile(stats, [alpha, 1 - alpha])
    return float(lo), float(hi)


def median_ratio(tok_target: Sequence[int], tok_reference: Sequence[int]) -> float:
    return float(np.median(sentence_parities(tok_target, tok_reference)))


def context_capacity(fertility_value: float, window: int = 4096) -> float:
    """Approximate number of words that fit into ``window`` tokens.

    >>> context_capacity(2.0)
    2048.0
    """
    if fertility_value <= 0:
        raise ValueError("fertility must be positive")
    return window / fertility_value


# ---------------------------------------------------------------- morphology


def gold_boundaries(segmentation: str, sep: str = "+") -> tuple[str, set[int]]:
    """Surface word and its internal morpheme boundaries as UTF-8 byte offsets.

    >>> word, b = gold_boundaries("kitob+lar+imiz+dan")
    >>> word, sorted(b)
    ('kitoblarimizdan', [5, 8, 12])
    >>> gold_boundaries("oʻg+il")  # ʻ is 2 bytes in UTF-8
    ('oʻgil', {4})
    """
    parts = segmentation.split(sep)
    if any(p == "" for p in parts):
        raise ValueError(f"empty morpheme in {segmentation!r}")
    offsets, pos = set(), 0
    for p in parts[:-1]:
        pos += len(p.encode("utf-8"))
        offsets.add(pos)
    return "".join(parts), offsets


def boundary_prf(
    predicted: Iterable[set[int]], gold: Iterable[set[int]]
) -> dict[str, float]:
    """Micro-averaged precision, recall and F1 of boundary sets (one set per word).

    A word with no gold boundary (``dollar``) only contributes false positives.

    >>> r = boundary_prf([{5, 8}, {2}], [{5, 8, 12}, set()])
    >>> round(r["precision"], 3), round(r["recall"], 3), round(r["f1"], 3)
    (0.667, 0.667, 0.667)
    """
    tp = fp = fn = 0
    for p, g in zip(predicted, gold):
        tp += len(p & g)
        fp += len(p - g)
        fn += len(g - p)
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {"precision": precision, "recall": recall, "f1": f1, "tp": tp, "fp": fp, "fn": fn}


# ---------------------------------------------------------------- tokenizer adapter


@lru_cache(maxsize=1)
def _byte_decoder() -> dict[str, int]:
    """Inverse of GPT-2's ``bytes_to_unicode`` table (byte-level BPE alphabet)."""
    bs = (
        list(range(ord("!"), ord("~") + 1))
        + list(range(ord("¡"), ord("¬") + 1))
        + list(range(ord("®"), ord("ÿ") + 1))
    )
    cs = bs[:]
    n = 0
    for b in range(256):
        if b not in bs:
            bs.append(b)
            cs.append(256 + n)
            n += 1
    return {chr(c): b for b, c in zip(bs, cs)}


_SP_BYTE = re.compile(r"^<0x([0-9A-Fa-f]{2})>$")


class TokenizerAdapter:
    """Uniform view on a Hugging Face tokenizer.

    Three token-string conventions are recognised from a probe text and mapped
    back to raw UTF-8 bytes, so that boundaries are comparable across tokenizers:

    * ``"sentencepiece"`` -- ``▁`` marks a space; ``<0xNN>`` is a byte-fallback token
      (XLM-R, mT5, Llama 2, Gemma)
    * ``"bytelevel"`` -- GPT-2 byte alphabet, ``Ġ`` is a space (GPT-2, Qwen, Llama 3,
      our own BPE)
    * ``"bytes"`` -- one token per byte, shown as a Latin-1 character (ByT5)
    """

    def __init__(self, tokenizer, name: str | None = None):
        self.tok = tokenizer
        self.name = name or getattr(tokenizer, "name_or_path", "tokenizer")
        self.scheme = self._detect_scheme()
        self._word_cache: dict[str, list[tuple[int, int]]] = {}

    # -- encoding ------------------------------------------------------------
    def ids(self, text: str) -> list[int]:
        return list(self.tok(text, add_special_tokens=False)["input_ids"])

    def count(self, texts: Sequence[str]) -> np.ndarray:
        """Number of tokens of each text (no special tokens)."""
        enc = self.tok(list(texts), add_special_tokens=False)["input_ids"]
        return np.array([len(x) for x in enc], dtype=np.int64)

    def _detect_scheme(self) -> str:
        toks = self.tok.convert_ids_to_tokens(self.ids("a b"))
        if any("▁" in t for t in toks):
            return "sentencepiece"
        if any("Ġ" in t for t in toks):
            return "bytelevel"
        if " " in toks:
            return "bytes"
        raise ValueError(f"{self.name}: unknown token convention {toks!r}")

    def _token_to_bytes(self, token: str) -> bytes:
        if self.scheme == "bytelevel":
            dec = _byte_decoder()
            return bytes(dec[c] for c in token)
        if self.scheme == "bytes":
            return token.encode("latin-1")
        m = _SP_BYTE.match(token)
        if m:
            return bytes([int(m.group(1), 16)])
        return token.replace("▁", " ").encode("utf-8")

    def token_bytes(self, text: str) -> list[bytes]:
        """Raw bytes of every token of ``text``; checked against the input."""
        pieces = [self._token_to_bytes(t) for t in self.tok.convert_ids_to_tokens(self.ids(text))]
        if b"".join(pieces).strip() != text.encode("utf-8").strip():
            raise ValueError(
                f"{self.name}: tokens do not reproduce the input "
                f"({b''.join(pieces)!r} vs {text.encode('utf-8')!r}); "
                "the tokenizer probably normalizes this text"
            )
        return pieces

    # -- per-word views --------------------------------------------------------
    def word_spans(self, word: str) -> list[tuple[int, int]]:
        """Byte spans (start, end) of the tokens covering ``word``.

        ``word`` is tokenized as ``" " + word``; offsets are relative to the first
        byte of the word, and tokens that contain only the leading space are dropped.
        """
        if word in self._word_cache:
            return self._word_cache[word]
        pieces = self.token_bytes(" " + word)
        n_word = len(word.encode("utf-8"))
        offset = len(b"".join(pieces)) - n_word
        spans, pos = [], -offset
        for p in pieces:
            start, end = pos, pos + len(p)
            pos = end
            if end > 0 and start < n_word:
                spans.append((max(start, 0), min(end, n_word)))
        self._word_cache[word] = spans
        return spans

    def n_word_tokens(self, word: str) -> int:
        return len(self.word_spans(word))

    def word_boundaries(self, word: str) -> set[int]:
        """Token boundaries strictly inside ``word`` as byte offsets."""
        n_word = len(word.encode("utf-8"))
        return {end for _, end in self.word_spans(word) if 0 < end < n_word}

    def word_pieces(self, word: str) -> list[str]:
        """Readable token pieces of ``word``; a broken UTF-8 character shows as ⟨CA⟩."""
        data = word.encode("utf-8")
        return [_readable(data[s:e]) for s, e in self.word_spans(word)]


def _readable(chunk: bytes) -> str:
    try:
        return chunk.decode("utf-8")
    except UnicodeDecodeError:
        out, i = [], 0
        while i < len(chunk):
            for j in range(min(len(chunk), i + 4), i, -1):
                try:
                    out.append(chunk[i:j].decode("utf-8"))
                    i = j
                    break
                except UnicodeDecodeError:
                    continue
            else:
                out.append(f"⟨{chunk[i]:02X}⟩")
                i += 1
        return "".join(out)


def continued_word_rate(adapter: TokenizerAdapter, word_list: Iterable[str]) -> float:
    """Share of word occurrences split into more than one token."""
    n = split = 0
    for w in word_list:
        n += 1
        split += adapter.n_word_tokens(w) > 1
    if n == 0:
        raise ValueError("no words in input")
    return split / n


def morph_alignment(adapter: TokenizerAdapter, segmentations: Sequence[str]) -> dict[str, float]:
    """Boundary P/R/F1 of ``adapter`` against gold segmentations like ``kitob+lar``."""
    gold = [gold_boundaries(s) for s in segmentations]
    pred = [adapter.word_boundaries(w) for w, _ in gold]
    return boundary_prf(pred, [g for _, g in gold])
