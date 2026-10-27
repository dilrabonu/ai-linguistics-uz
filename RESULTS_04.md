# §4 Tokenization & morphology — results

Source of every number below: one headless execution of
`notebooks/04_tokenization_audit.ipynb` (2026-10-27, CPU only), written to `results/04/*.csv`.
The tables in this file were generated from those CSVs. Rounding: 2 decimals.

> **The morphological alignment results use a DRAFT gold set** (`data/samples/morph_gold_uz.tsv`)
> that has not yet been verified by a linguist. Treat those numbers as preliminary.

## Data actually used

| Data | Subset | Size |
|---|---|---|
| FLORES-200 (official archive, CC BY-SA 4.0) | `uzn_Latn` + `eng_Latn`, dev + devtest, 1,000 indices sampled with seed 42 | 1,000 parallel sentence pairs (516 dev, 484 devtest) |
| Uzbek Wikipedia, `wikimedia/wikipedia` config `20231101.uz` | first 40,000 articles, normalized, kept if ≥ 90 % of letters are Latin | 38,912 articles, 26.1 M characters (1,088 dropped) |
| English Wikipedia, config `20231101.en` | first articles until the Uzbek character count is reached | 1,210 articles, 26.1 M characters |
| Gold morpheme segmentation (this project, DRAFT) | 29 noun, 31 verb, 12 derivation, 19 tricky, 9 one-morpheme words | 100 words, 159 gold boundaries |

FLORES was used through the official download, not the gated Hugging Face copy
(`openlanguagedata/flores_plus`), so no token is needed and the results do not depend on having one.
Licences and exact subsets: `data/DATA_SOURCES.md`.

## Tokenizers

Pretrained, ungated (tokenizer files only, no model weights): `gpt2`, `Qwen/Qwen2.5-0.5B`,
`xlm-roberta-base`, `google/mt5-small`, `google/byt5-small`.
**Not run:** `meta-llama/Llama-3.2-1B` and `google/gemma-3-1b-pt` (gated; no `HF_TOKEN` was set). The
notebook skips them with a message and includes them automatically when a token is available.

Own tokenizers (marked `*`): byte-level BPE trained with HF `tokenizers` on the normalized Uzbek Wikipedia
sample at 8k, 16k and 32k vocabulary (`BPE-uz-*`), and one 32k tokenizer trained on Uzbek + English
Wikipedia with equal character counts (`BPE-uz+en-32k`).

## Definitions (as implemented in `src/uzling/tokenizer_stats.py`)

- **Word:** a whitespace-separated chunk with leading/trailing punctuation and symbols (Unicode P\*, S\*)
  stripped; chunks that become empty are not words. ʻ and ʼ are letters (category Lm) and are never stripped.
- **Tokens:** counted on whole sentences with `add_special_tokens=False` (no BOS/EOS/CLS/SEP). Space-only
  tokens (a lone `▁`, ByT5's space byte) are counted, because they are real tokens.
- **Fertility** = total tokens / total words (corpus level). The mean of sentence-level fertility is in
  `main_table.csv`; it differs from the corpus value by at most 0.033 for every tokenizer.
- **Parity** = tokens(uz) / tokens(en) on the same 1,000 parallel sentences: corpus level (ratio of sums;
  primary) and the median of sentence-level ratios, each with a 95 % CI from 1,000 bootstrap resamples of
  sentence pairs (seed 42).
- **Continued-word rate** = share of word occurrences that take more than one token when tokenized as `" " + word`.
- **Bytes / characters per token** = UTF-8 bytes (characters) of the corpus / tokens.
- **Context capacity** = 4,096 / fertility = words that fit into a 4,096-token window.
- **Morphological alignment:** each gold word is tokenized as `" " + word`; token boundaries strictly inside
  the word are compared with gold morpheme boundaries as UTF-8 byte offsets; precision, recall and F1 are
  micro-averaged over all words. A boundary inside the 2-byte ʻ counts as a false boundary.

## Main results (normalized Uzbek, FLORES-200, 1,000 sentence pairs)

| Tokenizer | Vocab | Fertility uz | Fertility en | Parity (95% CI) | Median sentence parity (95% CI) | Continued words uz / en | Bytes/token uz | Words in 4,096 tokens uz / en | Morph. F1 |
|---|---:|---:|---:|---|---|---|---:|---|---:|
| GPT-2 | 50,257 | 3.56 | 1.23 | 2.38 (2.35–2.41) | 2.38 (2.34–2.42) | 89.9% / 6.9% | 2.34 | 1,150 / 3,323 | 0.30 |
| Qwen2.5 | 151,665 | 3.29 | 1.26 | 2.16 (2.13–2.18) | 2.16 (2.12–2.20) | 89.2% / 7.7% | 2.53 | 1,245 / 3,258 | 0.35 |
| XLM-R | 250,002 | 2.25 | 1.40 | 1.33 (1.31–1.34) | 1.32 (1.31–1.33) | 62.3% / 20.2% | 3.71 | 1,822 / 2,936 | 0.49 |
| mT5 | 250,100 | 2.55 | 1.53 | 1.37 (1.36–1.39) | 1.36 (1.35–1.38) | 76.9% / 18.9% | 3.26 | 1,604 / 2,674 | 0.50 |
| ByT5 | 384 | 8.33 | 6.01 | 1.14 (1.13–1.15) | 1.14 (1.12–1.15) | 99.3% / 97.7% | 1.00 | 491 / 682 | 0.34 |
| BPE-uz-8k* | 8,000 | 2.02 | 2.58 | 0.65 (0.64–0.65) † | 0.64 (0.64–0.65) † | 49.6% / 69.3% | 4.12 | 2,025 / 1,586 | 0.49 |
| BPE-uz-16k* | 16,000 | 1.78 | 2.38 | 0.62 (0.61–0.62) † | 0.62 (0.61–0.63) † | 38.7% / 66.0% | 4.69 | 2,303 / 1,724 | 0.43 |
| BPE-uz-32k* | 32,000 | 1.58 | 2.18 | 0.60 (0.59–0.60) † | 0.60 (0.59–0.61) † | 28.6% / 61.9% | 5.26 | 2,584 / 1,876 | 0.33 |
| BPE-uz+en-32k* | 32,000 | 1.75 | 1.35 | 1.07 (1.05–1.08) | 1.07 (1.05–1.08) | 38.0% / 13.7% | 4.77 | 2,347 / 3,033 | 0.43 |

† Monolingual Uzbek tokenizers: English parity is reported but **not meaningful**. They never saw English,
so English becomes expensive and parity falls below 1. The fertility figure shows only BPE-uz-32k, and the
parity figure omits all three.

## Raw vs normalized Uzbek (apostrophes)

FLORES `uzn_Latn` writes oʻ/gʻ and the tutuq belgisi with ASCII `'` (4,521 times in its 2,009 lines;
U+02BB 15 times, U+02BC twice). Normalization maps them to ʻ (U+02BB) / ʼ (U+02BC), 2 bytes each in UTF-8.

| Tokenizer | Tokens raw | Tokens normalized | Change | Parity raw → normalized | Sentences changed |
|---|---:|---:|---:|---|---:|
| GPT-2 | 59,676 | 62,136 | +4.1% | 2.29 → 2.38 | 872 / 1000 |
| Qwen2.5 | 56,837 | 57,382 | +1.0% | 2.14 → 2.16 | 394 / 1000 |
| XLM-R | 39,229 | 39,230 | +0.0% | 1.33 → 1.33 | 1 / 1000 |
| mT5 | 44,545 | 44,546 | +0.0% | 1.37 → 1.37 | 1 / 1000 |
| ByT5 | 143,136 | 145,411 | +1.6% | 1.13 → 1.14 | 872 / 1000 |
| BPE-uz-8k | 40,368 | 35,299 | -12.6% | 0.74 → 0.65 | 869 / 1000 |
| BPE-uz-16k | 36,368 | 31,033 | -14.7% | 0.72 → 0.62 | 872 / 1000 |
| BPE-uz-32k | 33,176 | 27,654 | -16.6% | 0.72 → 0.60 | 871 / 1000 |
| BPE-uz+en-32k | 35,888 | 30,455 | -15.1% | 1.26 → 1.07 | 869 / 1000 |

## Morphological alignment (DRAFT gold set, 100 words)

| Tokenizer | Precision | Recall | F1 | Exact word match | Tokens per gold word | False boundaries in 9 one-morpheme words |
|---|---:|---:|---:|---:|---:|---:|
| GPT-2 | 0.22 | 0.48 | 0.30 | 3% | 4.42 | 13 |
| Qwen2.5 | 0.27 | 0.48 | 0.35 | 8% | 3.85 | 12 |
| XLM-R | 0.50 | 0.49 | 0.49 | 23% | 2.57 | 5 |
| mT5 | 0.49 | 0.51 | 0.50 | 26% | 2.66 | 4 |
| ByT5 | 0.20 | 1.00 | 0.34 | 0% | 8.90 | 41 |
| BPE-uz-8k | 0.55 | 0.45 | 0.49 | 18% | 2.32 | 7 |
| BPE-uz-16k | 0.56 | 0.35 | 0.43 | 17% | 1.99 | 4 |
| BPE-uz-32k | 0.53 | 0.25 | 0.33 | 16% | 1.74 | 2 |
| BPE-uz+en-32k | 0.54 | 0.35 | 0.43 | 17% | 2.03 | 3 |

F1 by word category (the 9 one-morpheme words have no gold boundaries, so only their false boundaries are
informative; see the last column above):

| Tokenizer | noun (n=29) | verb (n=31) | deriv (n=12) | tricky (n=19) |
|---|---:|---:|---:|---:|
| GPT-2 | 0.34 | 0.26 | 0.49 | 0.21 |
| Qwen2.5 | 0.37 | 0.29 | 0.49 | 0.34 |
| XLM-R | 0.61 | 0.43 | 0.59 | 0.38 |
| mT5 | 0.54 | 0.50 | 0.50 | 0.46 |
| ByT5 | 0.30 | 0.42 | 0.32 | 0.34 |
| BPE-uz-8k | 0.46 | 0.55 | 0.74 | 0.31 |
| BPE-uz-16k | 0.37 | 0.51 | 0.61 | 0.24 |
| BPE-uz-32k | 0.24 | 0.46 | 0.36 | 0.21 |
| BPE-uz+en-32k | 0.53 | 0.42 | 0.52 | 0.20 |

Five illustrative words (`|` = token boundary; `⟨CA⟩⟨BB⟩` = the two UTF-8 bytes of ʻ in separate tokens):

| | `kitoblarimizdan` | `bolalar` | `dollar` | `yuragimda` | `oʻqituvchilarimizga` |
|---|---|---|---|---|---|
| **gold** | `kitob\|lar\|imiz\|dan` | `bola\|lar` | `dollar` | `yurag\|im\|da` | `oʻqi\|t\|uvchi\|lar\|imiz\|ga` |
| GPT-2 | `kit\|ob\|lar\|im\|iz\|dan` | `bol\|al\|ar` | `dollar` | `y\|ur\|ag\|im\|da` | `o\|⟨CA⟩\|⟨BB⟩\|q\|it\|uv\|ch\|ilar\|im\|iz\|ga` |
| Qwen2.5 | `kit\|ob\|lar\|im\|iz\|dan` | `bol\|alar` | `dollar` | `y\|ur\|ag\|im\|da` | `o\|ʻ\|q\|it\|uv\|ch\|ilar\|im\|iz\|ga` |
| XLM-R | `kitob\|larimiz\|dan` | `bolalar` | `dollar` | `y\|ura\|gim\|da` | `o\|ʻ\|qituvchilar\|imiz\|ga` |
| mT5 | `kito\|b\|larimiz\|dan` | `bola\|lar` | `dollar` | `yu\|ragi\|mda` | `o\|ʻ\|qituvchilar\|imizga` |
| ByT5 | `k\|i\|t\|o\|b\|l\|a\|r\|i\|m\|i\|z\|d\|a\|n` | `b\|o\|l\|a\|l\|a\|r` | `d\|o\|l\|l\|a\|r` | `y\|u\|r\|a\|g\|i\|m\|d\|a` | `o\|⟨CA⟩\|⟨BB⟩\|q\|i\|t\|u\|v\|c\|h\|i\|l\|a\|r\|i\|m\|i\|z\|g\|a` |
| BPE-uz-32k | `kitoblari\|mizdan` | `bolalar` | `dollar` | `yura\|gim\|da` | `oʻqituvchilari\|mizga` |
| BPE-uz+en-32k | `kitoblar\|imiz\|dan` | `bolalar` | `dollar` | `yur\|a\|gim\|da` | `oʻqituvchilar\|imiz\|ga` |

## Figures (`results/04/`, PNG 300 dpi + SVG; Uzbek labels; Okabe–Ito palette; DejaVu Sans)

1. `fig_fertility_uz_en` — Fertility on Uzbek vs English for the five pretrained tokenizers and our two 32k
   BPE tokenizers. Uzbek is higher for every pretrained tokenizer (3.56 vs 1.23 for GPT-2; 2.25 vs 1.40 for
   XLM-R); only our own tokenizers bring Uzbek fertility below 1.8.
2. `fig_parity` — Corpus parity with bootstrap 95 % CIs and a dashed line at 1.0. GPT-2 (2.38) and Qwen2.5
   (2.16) are far above 1; ByT5, XLM-R and mT5 lie between 1.14 and 1.37; the balanced uz+en BPE is at 1.07.
3. `fig_token_split_example` — Coloured token chunks for *Oʻzbekistonning poytaxti Toshkent shahri*
   (5 to 41 tokens) and *kitoblarimizdan* (2 to 15 tokens). GPT-2 and ByT5 split ʻ into two byte tokens;
   space-only tokens are drawn as ␣.
4. `fig_morph_alignment` — Boundary F1 (bars) with precision and recall (markers) for the same seven
   tokenizers. The best F1 is 0.50 (mT5); ByT5 reaches recall 1.00 at precision 0.20.
5. `fig_raw_vs_normalized` — Change in the Uzbek token count when ASCII apostrophes are normalized:
   +4.1 % for GPT-2, +1.0 % for Qwen2.5, +1.6 % for ByT5, +0.0 % for XLM-R and mT5, −16.6 % for BPE-uz-32k.

## Observations (grounded in the tables above)

1. **The Uzbek tax is mostly a tokenizer effect, not a language effect.** ByT5 counts bytes (1.00 bytes per
   token), so its parity of 1.14 is essentially the byte-length ratio of the Uzbek and English texts.
   GPT-2 (2.38) and Qwen2.5 (2.16) charge about twice that; XLM-R (1.33) and mT5 (1.37) are much closer
   to this floor.
2. **Context and cost.** With GPT-2, a 4,096-token window holds about 1,150 Uzbek words but 3,323 English
   words; with Qwen2.5, 1,245 vs 3,258. At the same price per token, the same content costs 2.38× (GPT-2)
   or 2.16× (Qwen2.5) more in Uzbek.
3. **English-centric tokenizers break up almost every Uzbek word:** GPT-2 splits 89.9 % of Uzbek word
   occurrences into several tokens (English: 6.9 %), Qwen2.5 89.2 % (7.7 %), XLM-R 62.3 % (20.2 %).
4. **The ʻ character has a measurable cost.** GPT-2 has no token for ʻ and spends two byte tokens on it;
   normalizing ASCII `'` to ʻ/ʼ raises its Uzbek token count by 4.1 % (parity 2.29 → 2.38), and Qwen2.5's
   by 1.0 %. XLM-R and mT5 have ʻ in their vocabularies (token counts change in 1 of 1,000 sentences).
   Conversely, our BPE trained on normalized text needs 16.6 % fewer tokens on normalized input than on raw
   input: the orthography at inference should match the orthography in training.
5. **A small, Uzbek-aware tokenizer removes the tax.** Trained on 26.1 M characters of Wikipedia,
   BPE-uz-32k reaches Uzbek fertility 1.58 (best pretrained: XLM-R, 2.25). The balanced BPE-uz+en-32k reaches
   parity 1.07 (95 % CI 1.05–1.08) with English fertility 1.35, close to XLM-R's 1.40, so parity ≈ 1 is
   achievable with a 32k vocabulary.
6. **Larger vocabularies align less with morphology.** For our Uzbek BPE, growing the vocabulary from 8k to
   32k lowers fertility from 2.02 to 1.58, but lowers boundary recall from 0.45 to 0.25 (F1 0.49 → 0.33),
   while precision stays at 0.53–0.56: frequent multi-morpheme chunks such as `kitoblari|mizdan` become
   single tokens.
7. **No tokenizer segments like a morphologist.** The best boundary F1 is about 0.5 (mT5 0.50, XLM-R 0.49,
   BPE-uz-8k 0.49), and at most 26 % of gold words are split exactly at their morpheme boundaries (mT5).
   GPT-2's precision is 0.22 (`kit|ob|lar|im|iz|dan`); only mT5 splits `bolalar` as `bola|lar`. The tricky
   category has the lowest F1 for every tokenizer except Qwen2.5 (lowest: verbs) and ByT5 (lowest: nouns).
8. **Stems are mostly left whole.** `dollar` is one token in every tokenizer except ByT5 and BPE-uz-8k
   (`d|ollar`); over the 9 one-morpheme words, false boundaries range from 2 (BPE-uz-32k) to 13 (GPT-2),
   and 41 for ByT5.

## Limitations and caveats

- **The gold set is a DRAFT** (100 words, one surface-segmentation convention, 8 rows flagged CHECK); every
  morphology number may change after linguist verification. Segmentation depth (e.g. `bil+im+li`) and the
  placement of alternations (`yurag+im`) are convention-dependent.
- **FLORES is translated from English** (WikiNews, WikiJunior and WikiVoyage sources); parity on other
  genres (social media, legal text) may differ. The bootstrap CIs reflect sentence sampling only, not the
  choice of corpus.
- Fertility depends on the word definition, and one Uzbek word often corresponds to several English words,
  so **compare languages with parity, not fertility**.
- The Wikipedia samples are the **first** articles in file order, not random samples; the English sample is
  only 1,210 (long) articles. Uzbek Wikipedia contains many bot-generated stubs. Our BPE settings are untuned
  (byte-level, `min_frequency=2`).
- Llama 3.2 and Gemma 3 tokenizers were **not measured** (gated; no token available).
- XLM-R and mT5 apply NFKC normalization internally. This does not affect token counts, but 2 FLORES words
  (e.g. `km²`) cannot be aligned byte by byte. All 100 gold words align for every tokenizer.
- The printed snippet `book_snippets/04_fertility.py` uses raw text, the 997 dev sentences and plain
  `split()` words, so its numbers differ slightly from this file (it prints GPT-2 parity 2.29, the same as
  the raw-text value above).

## Runtime (measured)

Final run under first-run conditions (empty `data/cache`, empty Hugging Face cache, all downloads included),
CPU only, tokenizer library limited to 2 threads (`RAYON_NUM_THREADS=2`, like a free Colab VM), Windows 11,
Python 3.11.15, 12-thread desktop CPU:

| Step | Seconds |
|---|---:|
| 0 setup | 0.1 |
| 1 FLORES download + sample | 4.9 |
| 2 tokenizers (download) | 27.6 |
| 3 audit of 5 tokenizers (incl. bootstrap) | 10.4 |
| 4a stream Wikipedia (uz + en) | 35.9 |
| 4b train 4 BPE tokenizers | 29.4 |
| 4c audit of own tokenizers | 6.3 |
| 5 morphology | 0.1 |
| 6 summary, CSVs, figures | 3.5 |
| **Total inside the notebook** | **118.9 (2.0 min)** |

`nbconvert --execute` wall time including kernel start: 124 s. Two earlier fresh runs with identical numbers
took 116 s and 177 s inside the notebook, so network speed and machine load move the total by about a minute.
**Colab was not measured.** Estimate for a free Colab CPU VM: add 1–2 minutes for cloning and
`pip install -r requirements-colab.txt`, and allow 2–3× slower compute: **about 6–10 minutes**, inside the
20-minute budget. A second run on the same VM reuses `data/cache/` and the Hugging Face cache.
