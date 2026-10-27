import numpy as np
import pytest

from uzling.tokenizer_stats import (
    TokenizerAdapter,
    _byte_decoder,
    bootstrap_ci,
    boundary_prf,
    context_capacity,
    continued_word_rate,
    corpus_fertility,
    corpus_parity,
    count_words,
    fertility,
    gold_boundaries,
    mean_sentence_fertility,
    median_ratio,
    morph_alignment,
    parity,
    sentence_parities,
    words,
)

OKINA = "ʻ"

# ---------------------------------------------------------------- fake tokenizers


class FakeTok:
    """Mimics the parts of a Hugging Face tokenizer that the adapter uses."""

    def __init__(self, split, bos=None):
        self.split = split
        self.bos = bos
        self.name_or_path = "fake"
        self.vocab: dict[str, int] = {}
        self.inv: dict[int, str] = {}

    def _ids(self, text, add_special_tokens):
        ids = []
        if add_special_tokens and self.bos:
            ids.append(self._id(self.bos))
        ids += [self._id(t) for t in self.split(text)]
        return ids

    def _id(self, t):
        if t not in self.vocab:
            self.vocab[t] = len(self.vocab)
            self.inv[self.vocab[t]] = t
        return self.vocab[t]

    def __call__(self, text, add_special_tokens=True):
        if isinstance(text, list):
            return {"input_ids": [self._ids(t, add_special_tokens) for t in text]}
        return {"input_ids": self._ids(text, add_special_tokens)}

    def convert_ids_to_tokens(self, ids):
        return [self.inv[i] for i in ids]


def sp_split(text, size=3):
    """SentencePiece-like: '▁' + chunks of ``size`` characters per word."""
    out = []
    for w in text.split():
        w = "▁" + w
        out += [w[i : i + size] for i in range(0, len(w), size)]
    return out


def sp_split_with_byte_fallback(text):
    """Like sp_split but every ʻ becomes two <0xNN> byte-fallback tokens."""
    out = []
    for t in sp_split(text, size=1):
        if t == OKINA:
            out += [f"<0x{b:02X}>" for b in t.encode("utf-8")]
        else:
            out.append(t)
    return out


_ENC = {b: c for c, b in _byte_decoder().items()}


def bytelevel_split(text, size=2):
    """GPT-2-like: bytes mapped to the byte alphabet, chunks of ``size`` bytes."""
    data = text.encode("utf-8")
    return ["".join(_ENC[b] for b in data[i : i + size]) for i in range(0, len(data), size)]


def bytes_split(text):
    return [bytes([b]).decode("latin-1") for b in text.encode("utf-8")]


# ---------------------------------------------------------------- words


def test_words_definition():
    assert words("Oʻzbekiston — katta mamlakat (2024-yil).") == [
        "Oʻzbekiston",
        "katta",
        "mamlakat",
        "2024-yil",
    ]
    assert words("«maʼno», togʻ!") == ["maʼno", "togʻ"]
    assert words("  ...  ") == []
    assert count_words("bir, ikki; uch.") == 3


def test_ascii_apostrophe_is_punctuation_at_word_edge():
    # Raw text: a trailing ASCII ' is stripped like a quote; the word count is unchanged.
    assert words("tog' 'salom'") == ["tog", "salom"]
    assert count_words("tog' 'salom'") == count_words(f"tog{OKINA} salom")


# ---------------------------------------------------------------- simple API


def _chars(s):
    return [c for c in s if not c.isspace()]


def test_fertility_and_parity():
    assert fertility(str.split, ["bir ikki uch"]) == 1.0
    assert fertility(_chars, ["ab cd"]) == 2.0
    assert parity(_chars, ["aaaa"], ["aa"]) == 2.0
    with pytest.raises(ValueError):
        parity(_chars, ["a"], ["a", "b"])
    with pytest.raises(ValueError):
        fertility(_chars, ["—"])


# ---------------------------------------------------------------- statistics


def test_corpus_vs_mean_sentence_fertility():
    tokens, n_words = [2, 10], [1, 10]
    assert corpus_fertility(tokens, n_words) == pytest.approx(12 / 11)
    assert mean_sentence_fertility(tokens, n_words) == pytest.approx((2 + 1) / 2)
    assert mean_sentence_fertility([3, 5], [0, 5]) == 1.0  # empty sentence skipped


def test_parity_functions():
    uz, en = [4, 6, 10], [2, 3, 10]
    assert corpus_parity(uz, en) == pytest.approx(20 / 15)
    assert sentence_parities(uz, en).tolist() == [2.0, 2.0, 1.0]
    assert median_ratio(uz, en) == 2.0
    with pytest.raises(ValueError):
        corpus_parity([1], [1, 2])
    with pytest.raises(ValueError):
        sentence_parities([1], [0])


def test_bootstrap_ci_is_seeded_and_brackets_estimate():
    rng = np.random.default_rng(0)
    uz = rng.integers(20, 60, 300)
    en = rng.integers(15, 40, 300)
    ci1 = bootstrap_ci(corpus_parity, [uz, en], n_boot=300, seed=7)
    ci2 = bootstrap_ci(corpus_parity, [uz, en], n_boot=300, seed=7)
    assert ci1 == ci2
    assert ci1[0] < corpus_parity(uz, en) < ci1[1]
    with pytest.raises(ValueError):
        bootstrap_ci(corpus_parity, [uz, en[:-1]])


def test_context_capacity():
    assert context_capacity(1.25, window=4096) == pytest.approx(3276.8)
    with pytest.raises(ValueError):
        context_capacity(0)


# ---------------------------------------------------------------- morphology


def test_gold_boundaries():
    assert gold_boundaries("kitob+lar+imiz+dan") == ("kitoblarimizdan", {5, 8, 12})
    assert gold_boundaries("dollar") == ("dollar", set())
    word, b = gold_boundaries(f"o{OKINA}qi+di+m")
    assert word == f"o{OKINA}qidim" and b == {5, 7}  # ʻ takes 2 bytes
    with pytest.raises(ValueError):
        gold_boundaries("kitob++lar")


def test_boundary_prf_edge_cases():
    perfect = boundary_prf([{5, 8}], [{5, 8}])
    assert perfect["f1"] == 1.0
    nothing = boundary_prf([set()], [set()])
    assert nothing == {"precision": 0.0, "recall": 0.0, "f1": 0.0, "tp": 0, "fp": 0, "fn": 0}
    false_split = boundary_prf([{3}], [set()])  # "dol|lar" for the stem "dollar"
    assert false_split["fp"] == 1 and false_split["precision"] == 0.0


# ---------------------------------------------------------------- adapter


def test_scheme_detection():
    assert TokenizerAdapter(FakeTok(sp_split)).scheme == "sentencepiece"
    assert TokenizerAdapter(FakeTok(bytelevel_split)).scheme == "bytelevel"
    assert TokenizerAdapter(FakeTok(bytes_split)).scheme == "bytes"
    with pytest.raises(ValueError):
        TokenizerAdapter(FakeTok(str.split))


@pytest.mark.parametrize(
    "split", [sp_split, sp_split_with_byte_fallback, bytelevel_split, bytes_split]
)
def test_token_bytes_reproduce_text(split):
    ad = TokenizerAdapter(FakeTok(split))
    text = f" O{OKINA}zbekistonning poytaxti"
    assert b"".join(ad.token_bytes(text)).strip() == text.encode("utf-8").strip()


def test_special_tokens_not_counted():
    ad = TokenizerAdapter(FakeTok(sp_split, bos="<s>"))
    assert ad.count(["kitob"]).tolist() == [2]  # "▁ki", "tob" -- no <s>
    assert ad.ids("kitob") == ad.tok("kitob", add_special_tokens=False)["input_ids"]


def test_word_spans_sentencepiece():
    ad = TokenizerAdapter(FakeTok(sp_split))
    # " kitoblar" -> "▁ki" "tob" "lar": the ▁ (space) is not part of the word
    assert ad.word_spans("kitoblar") == [(0, 2), (2, 5), (5, 8)]
    assert ad.word_boundaries("kitoblar") == {2, 5}
    assert ad.word_pieces("kitoblar") == ["ki", "tob", "lar"]


def test_space_only_token_dropped():
    ad = TokenizerAdapter(FakeTok(lambda t: ["▁"] + [c for c in t.strip()]))
    assert ad.n_word_tokens("ab") == 2
    assert ad.word_boundaries("ab") == {1}


def test_bytelevel_splits_inside_okina():
    ad = TokenizerAdapter(FakeTok(lambda t: bytelevel_split(t, size=3)))
    # " oʻq" = 20 6F CA BB 71 -> [20 6F CA] [BB 71]: a boundary inside the ʻ character
    assert ad.word_boundaries(f"o{OKINA}q") == {2}
    assert ad.word_pieces(f"o{OKINA}q") == ["o⟨CA⟩", "⟨BB⟩q"]


def test_bytes_scheme_every_byte_is_a_token():
    ad = TokenizerAdapter(FakeTok(bytes_split))
    assert ad.n_word_tokens("kitob") == 5
    assert ad.word_boundaries("kitob") == {1, 2, 3, 4}


def test_continued_word_rate():
    ad = TokenizerAdapter(FakeTok(sp_split))  # "▁"+word in 3-char chunks
    # "va" -> "▁va" (1 token), "kitob" -> "▁ki","tob" (2 tokens)
    assert continued_word_rate(ad, ["va", "kitob", "va", "kitob"]) == 0.5
    with pytest.raises(ValueError):
        continued_word_rate(ad, [])


def test_morph_alignment_with_morpheme_tokenizer():
    morphs = {"kitob", "lar", "imiz", "dan", "bola"}

    def morph_split(text):
        out = []
        for w in text.split():
            first = True
            while w:
                for m in sorted(morphs, key=len, reverse=True):
                    if w.startswith(m):
                        out.append(("▁" if first else "") + m)
                        w = w[len(m) :]
                        first = False
                        break
                else:
                    out.append(("▁" if first else "") + w[0])
                    w = w[1:]
                    first = False
        return out

    ad = TokenizerAdapter(FakeTok(morph_split))
    res = morph_alignment(ad, ["kitob+lar+imiz+dan", "bola+lar"])
    assert res["f1"] == 1.0
    res = morph_alignment(ad, ["dollar"])  # d|o|l|lar -> 3 false boundaries
    assert res["fp"] == 3 and res["precision"] == 0.0
