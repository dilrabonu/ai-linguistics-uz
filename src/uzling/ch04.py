"""Helpers for notebook 04 (§4 Tokenization and morphology).

Data loading with caching, the tokenizer audit, our own BPE tokenizers, the
morphological alignment experiment, the book figures and the auto-generated
observations. Heavy dependencies (transformers, datasets, tokenizers, pandas,
matplotlib) are imported inside the functions, so ``import uzling`` stays light.
"""

from __future__ import annotations

import json
import os
import random
import tarfile
import time
import urllib.request
from collections.abc import Sequence
from pathlib import Path

import numpy as np

from .normalize import normalize_uz, script_shares
from .tokenizer_stats import (
    TokenizerAdapter,
    _readable,
    bootstrap_ci,
    context_capacity,
    continued_word_rate,
    corpus_fertility,
    corpus_parity,
    count_words,
    gold_boundaries,
    mean_sentence_fertility,
    median_ratio,
    words,
)

SEED = 42
FLORES_URL = "https://dl.fbaipublicfiles.com/nllb/flores200_dataset.tar.gz"
WIKI_DATASET = "wikimedia/wikipedia"
WIKI_CONFIG_UZ = "20231101.uz"
WIKI_CONFIG_EN = "20231101.en"

#: Default tokenizers: display name -> Hugging Face model ID (all ungated).
DEFAULT_TOKENIZERS = {
    "GPT-2": "gpt2",
    "Qwen2.5": "Qwen/Qwen2.5-0.5B",
    "XLM-R": "xlm-roberta-base",
    "mT5": "google/mt5-small",
    "ByT5": "google/byt5-small",
}
#: Gated tokenizers, used only when an HF token is available.
GATED_TOKENIZERS = {
    "Llama 3.2": "meta-llama/Llama-3.2-1B",
    "Gemma 3": "google/gemma-3-1b-pt",
}

EXAMPLE_SENTENCE = "Oʻzbekistonning poytaxti Toshkent shahri"
EXAMPLE_WORD = "kitoblarimizdan"

# Okabe-Ito colour-blind-safe palette.
OKABE_ITO = ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
COLOR_UZ = "#D55E00"
COLOR_EN = "#0072B2"


# ---------------------------------------------------------------- paths and timing


def repo_root() -> Path:
    """Repository root: the first parent of this file that contains ``pyproject.toml``."""
    for p in Path(__file__).resolve().parents:
        if (p / "pyproject.toml").exists():
            return p
    return Path.cwd()


def cache_dir() -> Path:
    d = Path(os.environ.get("UZLING_CACHE", repo_root() / "data" / "cache"))
    d.mkdir(parents=True, exist_ok=True)
    return d


def results_dir() -> Path:
    d = repo_root() / "results" / "04"
    d.mkdir(parents=True, exist_ok=True)
    return d


class StepTimer:
    """Records wall-clock seconds per notebook step (written to ``runtime.json``)."""

    def __init__(self, t0: float | None = None):
        self.steps: dict[str, float] = {}
        self._t0 = t0 if t0 is not None else time.time()
        self._name: str | None = None
        self._start = 0.0

    def start(self, name: str) -> None:
        self.stop()
        self._name, self._start = name, time.time()

    def stop(self) -> None:
        if self._name is not None:
            self.steps[self._name] = self.steps.get(self._name, 0.0) + time.time() - self._start
            self._name = None

    def total(self) -> float:
        return time.time() - self._t0

    def save(self, path: Path, **extra) -> dict:
        self.stop()
        info = {"steps_seconds": {k: round(v, 1) for k, v in self.steps.items()}}
        info["total_seconds"] = round(self.total(), 1)
        info.update(extra)
        path.write_text(json.dumps(info, indent=2), encoding="utf-8")
        return info


def hf_token() -> str | None:
    """HF token from the environment or from Colab secrets; ``None`` if absent."""
    tok = os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN")
    if tok:
        return tok
    try:  # pragma: no cover - only in Colab
        from google.colab import userdata

        return userdata.get("HF_TOKEN")
    except Exception:
        return None


# ---------------------------------------------------------------- data: FLORES-200


def _download(url: str, dest: Path) -> Path:
    if not dest.exists():
        tmp = dest.with_suffix(dest.suffix + ".part")
        urllib.request.urlretrieve(url, tmp)
        tmp.replace(dest)
    return dest


def load_flores(
    langs: Sequence[str] = ("uzn_Latn", "eng_Latn"), n: int = 1000, seed: int = SEED
) -> dict:
    """Load ``n`` parallel FLORES-200 sentences (sampled from dev + devtest).

    The official FLORES-200 archive (CC BY-SA 4.0) is downloaded once into the
    cache. The same sentence indices are used for every language, so the result
    is parallel. Returns ``{"sentences": {lang: [...]}, "meta": {...}}``.
    """
    tar_path = _download(FLORES_URL, cache_dir() / "flores200_dataset.tar.gz")
    data: dict[str, list[str]] = {}
    split_sizes: dict[str, int] = {}
    with tarfile.open(tar_path, "r:gz") as tar:
        names = set(tar.getnames())
        for lang in langs:
            lines: list[str] = []
            for split in ("dev", "devtest"):
                member = f"./flores200_dataset/{split}/{lang}.{split}"
                if member not in names:
                    raise KeyError(f"{lang} not found in FLORES-200 ({member})")
                text = tar.extractfile(member).read().decode("utf-8")
                part = text.rstrip("\n").split("\n")
                split_sizes[split] = len(part)
                lines += part
            data[lang] = lines
    total = len(next(iter(data.values())))
    if any(len(v) != total for v in data.values()):
        raise ValueError("FLORES files are not parallel")
    idx = sorted(random.Random(seed).sample(range(total), n)) if n < total else list(range(total))
    n_dev = sum(1 for i in idx if i < split_sizes["dev"])
    return {
        "sentences": {lang: [data[lang][i] for i in idx] for lang in langs},
        "meta": {
            "source": FLORES_URL,
            "pool": total,
            "n": len(idx),
            "from_dev": n_dev,
            "from_devtest": len(idx) - n_dev,
            "seed": seed,
            "indices": idx,
        },
    }


# ---------------------------------------------------------------- data: Wikipedia


def _stream_wiki(config: str, keep, limit_fn, cache_name: str) -> tuple[list[str], dict]:
    cache = cache_dir() / cache_name
    meta_path = cache.with_suffix(".json")
    if cache.exists() and meta_path.exists():
        texts = cache.read_text(encoding="utf-8").split("\n")
        return texts, json.loads(meta_path.read_text(encoding="utf-8"))
    from datasets import load_dataset

    ds = load_dataset(WIKI_DATASET, config, split="train", streaming=True)
    texts, seen, dropped, chars = [], 0, 0, 0
    for row in ds:
        seen += 1
        text = " ".join(row["text"].split())  # one article per line
        text = keep(text)
        if text is None:
            dropped += 1
        else:
            texts.append(text)
            chars += len(text)
        if limit_fn(seen, chars):
            break
    meta = {
        "dataset": WIKI_DATASET,
        "config": config,
        "articles_read": seen,
        "articles_kept": len(texts),
        "articles_dropped": dropped,
        "characters": chars,
    }
    cache.write_text("\n".join(texts), encoding="utf-8")
    meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    return texts, meta


def load_wiki_uz(n_articles: int = 40_000, min_latin: float = 0.9) -> tuple[list[str], dict]:
    """First ``n_articles`` of Uzbek Wikipedia (streamed), normalized, Latin only.

    Articles whose letters are less than ``min_latin`` Latin (i.e. mostly Cyrillic
    or mixed) are dropped and counted in the returned metadata.
    """

    def keep(text: str) -> str | None:
        text = normalize_uz(text)
        if not text or script_shares(text)["latin"] < min_latin:
            return None
        return text

    texts, meta = _stream_wiki(
        WIKI_CONFIG_UZ,
        keep,
        lambda seen, _chars: seen >= n_articles,
        f"wiki_uz_{n_articles}_{min_latin}.txt",
    )
    meta["min_latin_share"] = min_latin
    return texts, meta


def load_wiki_en(char_budget: int) -> tuple[list[str], dict]:
    """English Wikipedia articles (streamed) until ``char_budget`` characters."""
    return _stream_wiki(
        WIKI_CONFIG_EN,
        lambda t: t or None,
        lambda _seen, chars: chars >= char_budget,
        f"wiki_en_{char_budget}.txt",
    )


# ---------------------------------------------------------------- tokenizers


def load_tokenizers(include_gated: bool = True) -> tuple[dict[str, TokenizerAdapter], dict]:
    """Load the default tokenizers, plus the gated ones if an HF token is available.

    Returns ``(adapters, info)``; ``info[name]`` holds the model ID, its kind and,
    for skipped tokenizers, the reason. Never falls back to unofficial mirrors.
    """
    from transformers import AutoTokenizer

    adapters: dict[str, TokenizerAdapter] = {}
    info: dict[str, dict] = {}
    for name, model_id in DEFAULT_TOKENIZERS.items():
        adapters[name] = TokenizerAdapter(AutoTokenizer.from_pretrained(model_id), name)
        info[name] = {"id": model_id, "kind": "pretrained", "status": "loaded"}
    token = hf_token() if include_gated else None
    for name, model_id in GATED_TOKENIZERS.items():
        if not token:
            info[name] = {"id": model_id, "kind": "gated", "status": "skipped: no HF_TOKEN"}
            continue
        try:
            tok = AutoTokenizer.from_pretrained(model_id, token=token)
            adapters[name] = TokenizerAdapter(tok, name)
            info[name] = {"id": model_id, "kind": "gated", "status": "loaded"}
        except Exception as e:  # licence not accepted, network, ...
            info[name] = {"id": model_id, "kind": "gated", "status": f"skipped: {type(e).__name__}"}
    for name, ad in adapters.items():
        info[name]["vocab_size"] = len(ad.tok)
        info[name]["scheme"] = ad.scheme
    return adapters, info


def train_bpe(texts: Sequence[str], vocab_size: int, name: str) -> TokenizerAdapter:
    """Train (or load from cache) a byte-level BPE tokenizer with HF ``tokenizers``.

    Byte-level like GPT-2/Qwen/Llama 3, so it has no unknown tokens and the same
    token conventions as the byte-level tokenizers it is compared with.
    """
    from tokenizers import Tokenizer, decoders, models, pre_tokenizers, trainers
    from transformers import PreTrainedTokenizerFast

    path = cache_dir() / "bpe" / f"{name}.json"
    if path.exists():
        tok = Tokenizer.from_file(str(path))
    else:
        tok = Tokenizer(models.BPE())
        tok.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)
        tok.decoder = decoders.ByteLevel()
        trainer = trainers.BpeTrainer(
            vocab_size=vocab_size,
            min_frequency=2,
            initial_alphabet=pre_tokenizers.ByteLevel.alphabet(),
            show_progress=False,
        )
        tok.train_from_iterator(texts, trainer=trainer, length=len(texts))
        path.parent.mkdir(parents=True, exist_ok=True)
        tok.save(str(path))
    return TokenizerAdapter(PreTrainedTokenizerFast(tokenizer_object=tok), name)


# ---------------------------------------------------------------- experiments


def audit(
    adapters: dict[str, TokenizerAdapter],
    uz: Sequence[str],
    en: Sequence[str],
    kinds: dict[str, str] | None = None,
    n_boot: int = 1000,
    window: int = 4096,
):
    """All §4 metrics per tokenizer on parallel ``uz``/``en`` sentences.

    Returns ``(table, sentence_counts)`` as pandas DataFrames.
    """
    import pandas as pd

    kinds = kinds or {}
    w_uz = np.array([count_words(s) for s in uz])
    w_en = np.array([count_words(s) for s in en])
    words_uz = [w for s in uz for w in words(s)]
    words_en = [w for s in en for w in words(s)]
    chars_uz, chars_en = sum(map(len, uz)), sum(map(len, en))
    bytes_uz = sum(len(s.encode("utf-8")) for s in uz)
    bytes_en = sum(len(s.encode("utf-8")) for s in en)
    rows, counts = [], {"words_uz": w_uz, "words_en": w_en}
    for name, ad in adapters.items():
        t_uz, t_en = ad.count(uz), ad.count(en)
        counts[f"{name}|uz"], counts[f"{name}|en"] = t_uz, t_en
        f_uz, f_en = corpus_fertility(t_uz, w_uz), corpus_fertility(t_en, w_en)
        p_lo, p_hi = bootstrap_ci(corpus_parity, [t_uz, t_en], n_boot=n_boot)
        m_lo, m_hi = bootstrap_ci(median_ratio, [t_uz, t_en], n_boot=n_boot)
        rows.append(
            {
                "tokenizer": name,
                "kind": kinds.get(name, "pretrained"),
                "vocab_size": len(ad.tok),
                "tokens_uz": int(t_uz.sum()),
                "tokens_en": int(t_en.sum()),
                "fertility_uz": f_uz,
                "fertility_en": f_en,
                "fertility_uz_sentence_mean": mean_sentence_fertility(t_uz, w_uz),
                "fertility_en_sentence_mean": mean_sentence_fertility(t_en, w_en),
                "parity": corpus_parity(t_uz, t_en),
                "parity_ci_low": p_lo,
                "parity_ci_high": p_hi,
                "parity_median": median_ratio(t_uz, t_en),
                "parity_median_ci_low": m_lo,
                "parity_median_ci_high": m_hi,
                "continued_word_rate_uz": continued_word_rate(ad, words_uz),
                "continued_word_rate_en": continued_word_rate(ad, words_en),
                "chars_per_token_uz": chars_uz / t_uz.sum(),
                "chars_per_token_en": chars_en / t_en.sum(),
                "bytes_per_token_uz": bytes_uz / t_uz.sum(),
                "bytes_per_token_en": bytes_en / t_en.sum(),
                f"context_words_uz_{window}": context_capacity(f_uz, window),
                f"context_words_en_{window}": context_capacity(f_en, window),
            }
        )
    return pd.DataFrame(rows), pd.DataFrame(counts)


def raw_vs_normalized(adapters: dict[str, TokenizerAdapter], uz_raw, uz_norm, en):
    """Token counts on raw vs apostrophe-normalized Uzbek (same English reference)."""
    import pandas as pd

    w = np.array([count_words(s) for s in uz_norm])
    t_en = None
    rows = []
    for name, ad in adapters.items():
        t_raw, t_norm, t_en = ad.count(uz_raw), ad.count(uz_norm), ad.count(en)
        rows.append(
            {
                "tokenizer": name,
                "tokens_raw": int(t_raw.sum()),
                "tokens_normalized": int(t_norm.sum()),
                "change_pct": 100 * (t_norm.sum() - t_raw.sum()) / t_raw.sum(),
                "fertility_raw": corpus_fertility(t_raw, w),
                "fertility_normalized": corpus_fertility(t_norm, w),
                "parity_raw": corpus_parity(t_raw, t_en),
                "parity_normalized": corpus_parity(t_norm, t_en),
                "sentences_changed": int(np.sum(t_raw != t_norm)),
            }
        )
    return pd.DataFrame(rows)


def load_morph_gold(path: Path | None = None) -> list[dict]:
    """Rows of ``data/samples/morph_gold_uz.tsv`` (comment and header lines skipped)."""
    path = path or repo_root() / "data" / "samples" / "morph_gold_uz.tsv"
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#") or line.startswith("word\t"):
            continue
        word, seg, notes = (line.split("\t") + [""])[:3]
        surface, _ = gold_boundaries(seg)
        if surface != word:
            raise ValueError(f"segmentation {seg!r} does not spell {word!r}")
        category = notes[1 : notes.index("]")] if notes.startswith("[") else ""
        rows.append({"word": word, "segmentation": seg, "category": category, "notes": notes})
    return rows


SHOWCASE_WORDS = ["kitoblarimizdan", "bolalar", "dollar", "yuragimda", "oʻqituvchilarimizga"]


def morph_scores(adapters: dict[str, TokenizerAdapter], gold: list[dict]):
    """Boundary P/R/F1 per tokenizer, per category, and showcase splits.

    Returns ``(overall, by_category, examples)`` DataFrames.
    """
    import pandas as pd

    from .tokenizer_stats import boundary_prf

    overall, by_cat, examples = [], [], []
    gold_b = {r["word"]: gold_boundaries(r["segmentation"])[1] for r in gold}
    for name, ad in adapters.items():
        pred = {r["word"]: ad.word_boundaries(r["word"]) for r in gold}
        res = boundary_prf([pred[w] for w in gold_b], list(gold_b.values()))
        exact = np.mean([pred[w] == gold_b[w] for w in gold_b])
        mean_tokens = np.mean([ad.n_word_tokens(w) for w in gold_b])
        overall.append(
            {"tokenizer": name, **res, "exact_match": exact, "tokens_per_word": mean_tokens}
        )
        for cat in sorted({r["category"] for r in gold}):
            ws = [r["word"] for r in gold if r["category"] == cat]
            res_c = boundary_prf([pred[w] for w in ws], [gold_b[w] for w in ws])
            by_cat.append({"tokenizer": name, "category": cat, "n_words": len(ws), **res_c})
        for w in SHOWCASE_WORDS:
            seg = next(r["segmentation"] for r in gold if r["word"] == w)
            examples.append(
                {
                    "word": w,
                    "gold": seg.replace("+", "|"),
                    "tokenizer": name,
                    "split": "|".join(ad.word_pieces(w)),
                    "exact": pred[w] == gold_b[w],
                    "correct_boundaries": len(pred[w] & gold_b[w]),
                    "gold_boundaries": len(gold_b[w]),
                    "false_boundaries": len(pred[w] - gold_b[w]),
                }
            )
    return pd.DataFrame(overall), pd.DataFrame(by_cat), pd.DataFrame(examples)


# ---------------------------------------------------------------- figures


def _thousands(x: float) -> str:
    """Integer with a space as thousands separator (4 096), as written in Uzbek."""
    return f"{x:,.0f}".replace(",", " ")


def uz_num(x: float, digits: int = 2) -> str:
    """Number with a decimal comma, as written in Uzbek (2,51)."""
    return f"{x:.{digits}f}".replace(".", ",")


def setup_style() -> None:
    import matplotlib as mpl

    mpl.rcParams.update(
        {
            "font.family": "DejaVu Sans",  # has ʻ (U+02BB) and ʼ (U+02BC)
            "font.size": 10,
            "axes.titlesize": 12,
            "axes.labelsize": 10,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "grid.alpha": 0.3,
            "axes.axisbelow": True,
            "figure.dpi": 100,
            "savefig.bbox": "tight",
            "svg.fonttype": "path",  # glyphs as paths: renders without the font installed
        }
    )


def _comma_axis(ax, axis: str = "y", digits: int = 1) -> None:
    from matplotlib.ticker import FuncFormatter

    fmt = FuncFormatter(lambda v, _p: uz_num(v, digits))
    (ax.yaxis if axis == "y" else ax.xaxis).set_major_formatter(fmt)


def save_fig(fig, name: str) -> list[Path]:
    """Save ``fig`` as PNG (300 dpi) and SVG in ``results/04``."""
    out = []
    for ext in ("png", "svg"):
        p = results_dir() / f"{name}.{ext}"
        fig.savefig(p, dpi=300 if ext == "png" else None)
        out.append(p)
    return out


def _hatch(kind: str) -> str:
    return "//" if kind == "own" else ""


def plot_fertility(table):
    """Grouped bars: fertility on Uzbek vs English per tokenizer (the 'Uzbek tax')."""
    import matplotlib.pyplot as plt

    df = table.reset_index(drop=True)
    x = np.arange(len(df))
    fig, ax = plt.subplots(figsize=(8.5, 4.2))
    w = 0.38
    b1 = ax.bar(x - w / 2, df.fertility_uz, w, color=COLOR_UZ, label="Oʻzbekcha (uzn_Latn)")
    b2 = ax.bar(
        x + w / 2,
        df.fertility_en,
        w,
        color=COLOR_EN,
        hatch="..",
        edgecolor="white",
        label="Inglizcha (eng_Latn)",
    )
    for bars in (b1, b2):
        for b in bars:
            ax.annotate(
                uz_num(b.get_height()),
                (b.get_x() + b.get_width() / 2, b.get_height()),
                ha="center",
                va="bottom",
                fontsize=8,
                xytext=(0, 2),
                textcoords="offset points",
            )
    ax.set_xticks(x, [_label(r) for r in df.itertuples()])
    ax.set_ylabel("Fertillik (soʻz boshiga tokenlar soni)")
    ax.set_xlabel("Tokenizator")
    ax.set_title("Oʻzbek tili soligʻi: bir xil matn, turlicha tokenlar soni")
    _comma_axis(ax)
    ax.legend(frameon=False, loc="upper left")
    fig.text(
        0.01,
        -0.08,
        "Manba: FLORES-200, 1 000 ta parallel jumla. * — oʻzimiz oʻqitgan BPE tokenizatorlari.",
        fontsize=8,
        color="0.3",
    )
    return fig


def _label(row) -> str:
    """Tick label: own tokenizers get a star; long names are wrapped (BPE-uz+en / 32k*)."""
    name = row.tokenizer + ("*" if getattr(row, "kind", "") == "own" else "")
    if name.startswith("BPE-"):
        head, _, size = name.rpartition("-")
        name = f"{head}\n{size}"
    return name


def plot_parity(table):
    """Horizontal bars: corpus parity with bootstrap 95% CI; line at 1.0."""
    import matplotlib.pyplot as plt

    df = table.sort_values("parity").reset_index(drop=True)
    y = np.arange(len(df))
    fig, ax = plt.subplots(figsize=(7.5, 0.45 * len(df) + 1.4))
    colors = [OKABE_ITO[i % len(OKABE_ITO)] for i in range(len(df))]
    err = np.vstack([df.parity - df.parity_ci_low, df.parity_ci_high - df.parity])
    ax.barh(
        y,
        df.parity,
        color=colors,
        hatch=[_hatch(k) for k in df.kind],
        edgecolor="white",
        xerr=err,
        capsize=3,
        error_kw={"elinewidth": 1},
    )
    for i, r in df.iterrows():
        ax.text(r.parity_ci_high + 0.03, i, uz_num(r.parity), va="center", fontsize=8)
    ax.axvline(1.0, color="0.2", linestyle="--", linewidth=1)
    ax.set_ylim(-1.0, len(df) - 0.5)
    ax.text(1.0, -0.75, " tenglik = 1,0", fontsize=8, color="0.2", va="center")
    ax.set_yticks(y, [_label(r) for r in df.itertuples()])
    ax.set_xlabel("Parity: oʻzbekcha tokenlar / inglizcha tokenlar (95% ishonch oraligʻi)")
    ax.set_title("Tillararo tenglik (parity)")
    ax.set_xlim(0, max(df.parity_ci_high) * 1.15)
    ax.grid(axis="y", visible=False)
    _comma_axis(ax, "x")
    return fig


def plot_token_split(adapters: dict[str, TokenizerAdapter], sentence: str, word: str):
    """Coloured token chunks for ``sentence`` (all tokens) and ``word`` per tokenizer.

    Space-only tokens (a lone ``▁`` in SentencePiece, the space byte in ByT5) are real
    tokens: they are drawn as grey ``␣`` boxes and counted. The word panel shows the
    tokens that cover the word itself (see ``TokenizerAdapter.word_pieces``).
    """
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyBboxPatch

    names = list(adapters)
    panels = []  # (pieces, starts_with_space) per tokenizer and panel
    for name in names:
        ad = adapters[name]
        sent = [_readable(p) for p in ad.token_bytes(sentence)]
        panels.append([(p.strip() or "␣", p.startswith(" ") and bool(p.strip())) for p in sent])
        panels.append([(p, False) for p in ad.word_pieces(word)])

    def width(label: str) -> float:
        return max(len(label), 1) + 0.3

    def extent(pieces) -> float:
        return sum(width(lab) + 0.08 + (0.5 if gap else 0) for lab, gap in pieces)

    span = [max(extent(panels[2 * i + j]) for i in range(len(names))) + 7 for j in range(2)]
    fig, axes = plt.subplots(
        len(names),
        2,
        figsize=(sum(span) * 0.105 + 1.5, 0.5 * len(names) + 0.9),
        gridspec_kw={"width_ratios": span, "wspace": 0.05},
    )
    axes = np.atleast_2d(axes)
    for i, name in enumerate(names):
        for j in range(2):
            ax, pieces = axes[i, j], panels[2 * i + j]
            x = 0.0
            for k, (label, gap) in enumerate(pieces):
                x += 0.5 if gap else 0
                w = width(label)
                space = label == "␣"
                ax.add_patch(
                    FancyBboxPatch(
                        (x, 0.1),
                        w,
                        0.8,
                        boxstyle="round,pad=0.02,rounding_size=0.15",
                        facecolor="0.85" if space else OKABE_ITO[k % len(OKABE_ITO)],
                        alpha=1.0 if space else 0.55,
                        edgecolor="0.3",
                        linewidth=0.5,
                    )
                )
                ax.text(
                    x + w / 2,
                    0.5,
                    label,
                    ha="center",
                    va="center",
                    fontsize=9,
                    color="0.4" if space else "black",
                )
                x += w + 0.08
            ax.text(x + 0.4, 0.5, f"{len(pieces)} token", ha="left", va="center", fontsize=9)
            ax.set_xlim(-0.2, span[j])
            ax.set_ylim(0, 1)
            ax.axis("off")
        axes[i, 0].text(-0.5, 0.5, name, ha="right", va="center", fontsize=9, fontweight="bold")
    axes[0, 0].set_title(f"«{sentence}»", fontsize=11, loc="left")
    axes[0, 1].set_title(f"«{word}»", fontsize=11, loc="left")
    fig.suptitle("Tokenizatorlar bir xil matnni qanday boʻlaklarga ajratadi", fontsize=12, y=1.02)
    fig.text(
        0.01,
        -0.03,
        "⟨CA⟩⟨BB⟩ — ʻ belgisining UTF-8 dagi ikki bayti alohida tokenlarga ajralgan; "
        "␣ — faqat boʻshliqdan iborat token.",
        fontsize=8,
        color="0.3",
    )
    return fig


def plot_morph(overall):
    """Bars: boundary F1 per tokenizer, with precision and recall as markers."""
    import matplotlib.pyplot as plt

    df = overall.sort_values("f1", ascending=False).reset_index(drop=True)
    x = np.arange(len(df))
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(
        x,
        df.f1,
        color=OKABE_ITO[2],
        label="F1",
        hatch=[_hatch(k) for k in df.get("kind", [""] * len(df))],
        edgecolor="white",
    )
    ax.plot(x, df.precision, "o", color="0.15", label="Aniqlik (precision)")
    ax.plot(x, df.recall, "^", color=OKABE_ITO[5], label="Toʻliqlik (recall)")
    for i, v in enumerate(df.f1):
        ax.text(
            i,
            v / 2,
            uz_num(v),
            ha="center",
            va="center",
            fontsize=8,
            color="white",
            fontweight="bold",
        )
    ax.set_xticks(x, [_label(r) for r in df.itertuples()])
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("Morfema chegaralari bilan moslik")
    ax.set_title("Token chegaralari morfema chegaralariga qanchalik mos keladi")
    _comma_axis(ax)
    ax.legend(frameon=False, loc="upper right", fontsize=8)
    fig.text(
        0.01,
        -0.08,
        "100 ta qoʻlda segmentlangan soʻz (QORALAMA, tilshunos tekshiruvi "
        "kutilmoqda). * — oʻzimiz oʻqitgan BPE.",
        fontsize=8,
        color="0.3",
    )
    return fig


def plot_raw_vs_normalized(rvn, kinds: dict[str, str] | None = None):
    """Bars: % change in Uzbek token count after apostrophe normalization."""
    import matplotlib.pyplot as plt

    kinds = kinds or {}
    df = rvn.reset_index(drop=True)
    x = np.arange(len(df))
    fig, ax = plt.subplots(figsize=(8, 3.8))
    colors = [COLOR_UZ if v > 0 else COLOR_EN for v in df.change_pct]
    ax.bar(
        x,
        df.change_pct,
        color=colors,
        edgecolor="white",
        hatch=[_hatch(kinds.get(t, "")) for t in df.tokenizer],
    )
    for i, v in enumerate(df.change_pct):
        ax.text(
            i,
            v,
            f"{'+' if v > 0 else ''}{uz_num(v, 1)}%",
            ha="center",
            va="bottom" if v >= 0 else "top",
            fontsize=8,
        )
    ax.axhline(0, color="0.2", linewidth=0.8)
    ax.set_xticks(x, [_label(r) for r in df.assign(kind=df.tokenizer.map(kinds)).itertuples()])
    ax.set_ylabel("Tokenlar soni oʻzgarishi, %")
    ax.set_title("Apostrofni normallashtirish (' → ʻ / ʼ) tokenlar soniga taʼsiri")
    _comma_axis(ax)
    fig.text(
        0.01,
        -0.08,
        "Musbat: normallashtirilgan matn koʻproq token oladi; manfiy: kamroq. "
        "FLORES-200, 1 000 ta jumla. * — oʻzimiz oʻqitgan BPE.",
        fontsize=8,
        color="0.3",
    )
    return fig


# ---------------------------------------------------------------- observations


def observations(table, rvn, morph, own_names: Sequence[str] = ()) -> list[tuple[str, str]]:
    """Factual statements generated from the result tables: (Uzbek, English) pairs."""
    obs: list[tuple[str, str]] = []
    pre = table[table.kind != "own"]
    hi = pre.loc[pre.parity.idxmax()]
    lo = pre.loc[pre.parity.idxmin()]
    obs.append(
        (
            f"Eng katta „soliq“ {hi.tokenizer} tokenizatorida: oʻzbekcha matn inglizcha "
            f"tarjimasidan {uz_num(hi.parity)} baravar koʻp token oladi "
            f"(95% ishonch oraligʻi {uz_num(hi.parity_ci_low)}–{uz_num(hi.parity_ci_high)}).",
            f"The largest tax is in {hi.tokenizer}: Uzbek needs {hi.parity:.2f}x the tokens of the "
            f"English translation (95% CI {hi.parity_ci_low:.2f}-{hi.parity_ci_high:.2f}).",
        )
    )
    obs.append(
        (
            f"Eng kichik farq {lo.tokenizer} tokenizatorida: parity {uz_num(lo.parity)}.",
            f"The smallest gap is in {lo.tokenizer}: parity {lo.parity:.2f}.",
        )
    )
    ctx = [c for c in table.columns if c.startswith("context_words_uz_")][0]
    window = ctx.rsplit("_", 1)[1]
    cap_uz, cap_en = hi[ctx], hi[ctx.replace("_uz_", "_en_")]
    obs.append(
        (
            f"{hi.tokenizer} bilan {window} tokenli kontekstga taxminan {_thousands(cap_uz)} ta "
            f"oʻzbekcha soʻz sigʻadi, inglizcha esa {_thousands(cap_en)} ta.",
            f"With {hi.tokenizer}, a {window}-token window holds about {cap_uz:,.0f} Uzbek words "
            f"vs {cap_en:,.0f} English words.",
        )
    )
    worst = pre.loc[pre.continued_word_rate_uz.idxmax()]
    cwr_uz, cwr_en = 100 * worst.continued_word_rate_uz, 100 * worst.continued_word_rate_en
    obs.append(
        (
            f"{worst.tokenizer} oʻzbekcha soʻzlarning {uz_num(cwr_uz, 0)} foizini bir nechta "
            f"tokenga boʻladi (inglizchada {uz_num(cwr_en, 0)} foiz).",
            f"{worst.tokenizer} splits {cwr_uz:.0f}% of Uzbek words into several tokens "
            f"({cwr_en:.0f}% for English).",
        )
    )
    r = rvn[~rvn.tokenizer.isin(own_names)]
    big = r.loc[r.change_pct.abs().idxmax()]
    sign = "oshadi" if big.change_pct > 0 else "kamayadi"
    obs.append(
        (
            f"Apostrofni normallashtirish {big.tokenizer} da tokenlar sonini "
            f"{uz_num(abs(big.change_pct), 1)}% ga {sign}.",
            f"Normalizing apostrophes changes the {big.tokenizer} token count by "
            f"{big.change_pct:+.1f}%.",
        )
    )
    best, worst = morph.loc[morph.f1.idxmax()], morph.loc[morph.f1.idxmin()]
    obs.append(
        (
            f"Morfema chegaralariga eng mos tokenizator — {best.tokenizer} (F1 {uz_num(best.f1)}), "
            f"eng kam mosi — {worst.tokenizer} (F1 {uz_num(worst.f1)}); natijalar qoralama "
            f"oltin toʻplamga asoslangan.",
            f"Best morphological alignment: {best.tokenizer} (F1 {best.f1:.2f}); worst: "
            f"{worst.tokenizer} (F1 {worst.f1:.2f}) -- on the DRAFT gold set.",
        )
    )
    own = table[table.tokenizer.isin(own_names)]
    if len(own):
        o = own.loc[own.fertility_uz.idxmin()]
        obs.append(
            (
                f"Oʻzimiz oʻqitgan {o.tokenizer} oʻzbekcha fertilligi {uz_num(o.fertility_uz)}; "
                f"eng yaxshi tayyor tokenizatorda {uz_num(pre.fertility_uz.min())}.",
                f"Our own {o.tokenizer} reaches Uzbek fertility {o.fertility_uz:.2f}; the best "
                f"pretrained tokenizer reaches {pre.fertility_uz.min():.2f}.",
            )
        )
    return obs
