# Data sources

Every dataset used in a notebook is listed here **before** it is used. Large files are never
committed; notebooks download them at run time. Small evaluation sets created in this project
live in `data/<name>/` under CC BY 4.0.

| Dataset | Used in | Languages / script | Licence | Link | Notes |
|---|---|---|---|---|---|
| Wikipedia (Uzbek dump via `wikimedia/wikipedia`) | Ch. 2, 4, 5 | uz (Latin, some Cyrillic) | CC BY-SA 4.0 | https://huggingface.co/datasets/wikimedia/wikipedia | Streamed, not stored |
| FLORES-200 | Ch. 4, 10, 12 | 200 languages incl. `uzn_Latn` | CC BY-SA 4.0 | https://github.com/facebookresearch/flores | Parallel sentences |
| Belebele | Ch. 10, 11 | 122 language variants | CC BY-SA 4.0 | https://huggingface.co/datasets/facebook/belebele | Parallel reading comprehension |

_To verify before each release: licence text, version/date accessed, exact split used._

## Datasets created in this project

| Name | Chapter | Size | Method | Status |
|---|---|---|---|---|
| Uzbek minimal pairs | 6 | target 500 | Hand-written by linguists, double-checked | planned |
| Uzbek idioms and proverbs test | 9 | target 100+ | Dictionary-sourced, expert-annotated | planned |
| Uzbek culture QA (UzCulture-mini) | 12 | target 200 | Expert-written with references | planned |

Rules: no personal data of real people; record annotators' agreement (Cohen's kappa) for every
annotated set; publish a datasheet (Gebru et al., 2021) alongside each set.
