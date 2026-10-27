# Data sources

Every dataset used in a notebook is listed here **before** it is used. Large files are never
committed; notebooks download them at run time into `data/cache/` (git-ignored). Small evaluation
sets created in this project live in `data/samples/` under CC BY 4.0.

| Dataset | Used in | Languages / script | Licence | Link | Notes |
|---|---|---|---|---|---|
| Wikipedia (`wikimedia/wikipedia`) | Ch. 2, 4, 5 | uz (Latin, some Cyrillic); en | CC BY-SA 4.0 and GFDL (Wikimedia terms; the HF card lists CC BY-SA 3.0 + GFDL) | https://huggingface.co/datasets/wikimedia/wikipedia | Streamed; not redistributed |
| FLORES-200 | Ch. 4, 10, 12 | 200 languages incl. `uzn_Latn` | CC BY-SA 4.0 | https://github.com/facebookresearch/flores | Parallel sentences |
| Belebele | Ch. 10, 11 | 122 language variants | CC BY-SA 4.0 | https://huggingface.co/datasets/facebook/belebele | Parallel reading comprehension |

_To verify before each release: licence text, version/date accessed, exact split used._

## Exactly what §4 uses (notebook `04_tokenization_audit.ipynb`)

Accessed 2026-10-27.

| Source | Exact subset | Size used | How it is selected |
|---|---|---|---|
| FLORES-200, official archive `https://dl.fbaipublicfiles.com/nllb/flores200_dataset.tar.gz` (25.6 MB, `Last-Modified: 2022-07-14`) | `dev/{uzn_Latn,eng_Latn}.dev` (997 lines) + `devtest/…devtest` (1,012 lines) | **1,000 sentence pairs** (516 from dev, 484 from devtest) | `random.Random(42).sample(range(2009), 1000)`, same indices for both languages. Not gated, no login. The HF copy `openlanguagedata/flores_plus` is gated (auto-approval) and is not used, so results do not depend on having a token. |
| Wikipedia, config `20231101.uz` (the only Uzbek dump on the Hub; one 210 MB parquet file) | First 40,000 articles in file order (`N_WIKI_ARTICLES`) | **38,912 articles, 26.1 M characters** after normalization; 1,088 dropped as < 90 % Latin script | Streamed with `datasets`; apostrophes normalized with `uzling.normalize_uz`; whitespace collapsed. Used only to train our BPE tokenizers. |
| Wikipedia, config `20231101.en` | First articles in file order until the Uzbek character count is reached | **1,210 articles, 26.1 M characters** | Streamed. Used only for the balanced uz+en 32k BPE tokenizer. |

Tokenizers (files only, no model weights) are downloaded from the Hugging Face Hub: `gpt2` (MIT),
`Qwen/Qwen2.5-0.5B` (Apache-2.0), `xlm-roberta-base` (MIT), `google/mt5-small` (Apache-2.0),
`google/byt5-small` (Apache-2.0). Optional, only with `HF_TOKEN` and an accepted licence:
`meta-llama/Llama-3.2-1B` (Llama 3.2 Community License), `google/gemma-3-1b-pt` (Gemma Terms of Use).
Unofficial mirrors of gated models are never used.

## Datasets created in this project

| Name | Chapter | Size | Method | Status |
|---|---|---|---|---|
| Uzbek morpheme segmentation gold set (`data/samples/morph_gold_uz.tsv`) | 4 | 100 words | Drafted with an AI assistant; surface segmentation with Leipzig-style glosses | **DRAFT — requires verification by a linguist** |
| Uzbek minimal pairs | 6 | target 500 | Hand-written by linguists, double-checked | planned |
| Uzbek idioms and proverbs test | 9 | target 100+ | Dictionary-sourced, expert-annotated | planned |
| Uzbek culture QA (UzCulture-mini) | 12 | target 200 | Expert-written with references | planned |

Rules: no personal data of real people; record annotators' agreement (Cohen's kappa) for every
annotated set; publish a datasheet (Gebru et al., 2021) alongside each set.
