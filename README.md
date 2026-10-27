<div align="center">

# AI Linguistics for Uzbek
### *Sun'iy intellekt lingvistikasi* — open course materials

**How do large language models handle language — and what happens when that language is Uzbek?**

[![CI](https://github.com/dilrabonu/ai-linguistics-uz/actions/workflows/ci.yml/badge.svg)](https://github.com/dilrabonu/ai-linguistics-uz/actions/workflows/ci.yml)
[![Code: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE)
[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)](LICENSE-CONTENT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](pyproject.toml)

[O'zbekcha](README.uz.md) · [Chapters](#chapters) · [Quick start](#quick-start) · [Glossary](glossary/) · [Cite](#citation)

</div>

---

## Why this exists

Most NLP textbooks teach language technology through English. Uzbek — a Turkic language with
more than 30 million speakers, written in both Latin and Cyrillic script, with rich
agglutinative morphology — behaves very differently inside today's language models:

- **It costs more.** The same sentence is split into more tokens than its English translation.
- **It is under-represented.** Uzbek is a small fraction of web-scale training data.
- **Models can be confidently wrong in it.** Reliability and calibration often drop for low-resource languages.

This repository accompanies the Uzbek-language textbook ***Sun'iy intellekt lingvistikasi***
(AI Linguistics) and turns every chapter into a runnable notebook, an open dataset or a reusable tool.
It is written for **linguists who want to understand LLMs** and **engineers who want to understand language**.

## What is inside

| Folder | Contents |
|---|---|
| [`notebooks/`](notebooks/) | 14 Colab notebooks, one per chapter; each runs on free Colab in under 20 minutes |
| [`src/uzling/`](src/uzling/) | A small, tested Python package: apostrophe normalization, Cyrillic→Latin transliteration, tokenizer fertility & parity, calibration metrics (ECE, MCE, Brier) |
| [`glossary/`](glossary/) | An English–Uzbek glossary of AI and NLP terms with definitions (CC BY 4.0) |
| [`data/`](data/) | Small open evaluation sets built in the course, with full provenance in [`DATA_SOURCES.md`](data/DATA_SOURCES.md) |
| [`slides/`](slides/) | Lecture slides for instructors |
| [`docs/`](docs/) | Course roadmap and teaching notes |

## Chapters

| # | Chapter | Notebook | You will build | Status |
|---|---|---|---|---|
| 1 | What is AI linguistics? | [01](notebooks/01_what_is_ai_linguistics.ipynb) | An Uzbek ELIZA vs. a modern LLM | planned |
| 2 | Language as a sign system; text as numbers | [02](notebooks/02_text_as_numbers.ipynb) | An apostrophe audit and Zipf curves for Uzbek | **draft** |
| 3 | Uzbek through the eyes of a machine | [03](notebooks/03_uzbek_for_machines.ipynb) | A morphological segmenter; a gender-bias test for MT | planned |
| 4 | Tokenization and morphology | [04](notebooks/04_tokenization_audit.ipynb) | A tokenizer fairness audit ("the Uzbek token tax") | planned |
| 5 | Lexicon, semantics, embeddings | [05](notebooks/05_embeddings_uz.ipynb) | Homonyms in contextual embedding space | planned |
| 6 | Syntax and language models | [06](notebooks/06_language_models.ipynb) | Uzbek minimal pairs (BLiMP-style) | planned |
| 7 | Large language models | [07](notebooks/07_llms_in_uzbek.ipynb) | Prompt language × few-shot experiments | planned |
| 8 | Corpora and data quality | [08](notebooks/08_corpus_quality.ipynb) | A web-corpus cleaning pipeline + datasheet | planned |
| 9 | Pragmatics and figurative language | [09](notebooks/09_pragmatics_test.ipynb) | Idiom, honorific and implicature tests | planned |
| 10 | Multilinguality and Turkic languages | [10](notebooks/10_turkic_multilingual.ipynb) | A model's "language tree" vs. the linguists' tree | planned |
| 11 | Reliability, hallucination, calibration | [11](notebooks/11_calibration.ipynb) | Reliability diagrams, Uzbek vs. English | planned |
| 12 | Evaluation and benchmarks | [12](notebooks/12_evaluation.ipynb) | BLEU vs. chrF vs. human judgement | planned |
| 13 | Ethics and language policy | [13](notebooks/13_ethics_audit.ipynb) | A stereotype audit and a model card | planned |
| 14 | Future directions and capstone | [14](notebooks/14_capstone_rag.ipynb) | A small RAG assistant over Uzbek documents | planned |

## Quick start

**In the browser:** open any notebook above and click *Open in Colab*. The first cell installs everything.

**Locally:**

```bash
git clone https://github.com/dilrabonu/ai-linguistics-uz.git
cd ai-linguistics-uz
python -m venv .venv && source .venv/bin/activate
pip install -e ".[notebooks,dev]"
pytest            # runs unit tests and doctests
jupyter lab notebooks/
```

**Use the utilities in your own project:**

```python
from uzling import normalize_uz, cyr_to_lat, ece

normalize_uz("O`zbekiston") == normalize_uz("O'zbekiston")   # True: one canonical spelling
ece(confidence=[0.9, 0.8, 0.6], correct=[1, 0, 1])          # expected calibration error
```

## Design principles

1. **Uzbek first.** Every concept is introduced with an Uzbek example; English appears for comparison.
2. **Runs anywhere.** Free Colab, open-weight models, no paid API required.
3. **Reproducible.** Pinned dependencies, fixed seeds, tested utilities, documented data provenance.
4. **Linguistics and engineering together.** Each chapter has a *linguist's view* and an *engineer's view*.
5. **Open.** Code under MIT, text and data under CC BY 4.0 unless a source licence says otherwise.

## Model licences

Every notebook runs with **openly downloadable models and tokenizers only** — no Hugging Face account,
token or licence acceptance is needed. The default set is Qwen2.5, XLM-R and mT5 (plus GPT-2 and ByT5 as
baselines). Llama and Gemma require accepting their licences on Hugging Face, so they are **optional
extras**: a notebook uses them only if an `HF_TOKEN` is set and the licence was accepted, and otherwise
skips them with a message. All results and figures in the book come from the open models. Unofficial
mirrors of gated models are never used.

## Who is this for

- Linguistics and philology students who want to understand how LLMs work
- Computer science and AI students who want to understand language
- Researchers working on Uzbek, Turkic and other low-resource languages
- Instructors who want a ready-made, adaptable course

## Used in teaching

Planned pilot at **IT Park University (Tashkent)**. Instructors using these materials elsewhere are
warmly invited to open an issue so the list can be updated.

## Contributing

Corrections and new Uzbek examples are very welcome — especially glossary improvements,
dialect data and translations of the notebooks into other Turkic languages.
See [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md).

## Citation

If you use these materials, please cite them (GitHub's *Cite this repository* button reads
[`CITATION.cff`](CITATION.cff)):

```bibtex
@misc{khidirova_ai_linguistics_uz,
  author       = {Khidirova, Dilrabo},
  title        = {AI Linguistics for Uzbek: open course materials for
                  "Sun'iy intellekt lingvistikasi"},
  year         = {2026},
  howpublished = {\url{https://github.com/dilrabonu/ai-linguistics-uz}}
}
```

## Author

**Dilrabo Khidirova** — Senior Lecturer in Machine Learning, IT Park University, Tashkent.
Research: trustworthy AI, uncertainty and calibration for low-resource and Turkic languages.
ORCID: [0009-0009-4983-1503](https://orcid.org/0009-0009-4983-1503)

## License

Code: [MIT](LICENSE). Text, glossary and datasets created in this project: [CC BY 4.0](LICENSE-CONTENT).
Third-party datasets keep their original licences — see [`data/DATA_SOURCES.md`](data/DATA_SOURCES.md).
