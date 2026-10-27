# Contributing

Thank you for helping make AI linguistics accessible in Uzbek! Contributions in **English or Uzbek** are welcome.

## Ways to help

| You are a... | Good first contributions |
|---|---|
| Linguist | Fix or extend the glossary, add Uzbek examples, idioms, proverbs, minimal pairs, dialect data |
| Engineer | Improve `uzling`, add tests, make notebooks faster or more robust |
| Instructor | Report where students got stuck, share slides or exercises |
| Speaker of another Turkic language | Translate notebook explanations, add parallel examples |

## Workflow

1. Open an issue first for anything larger than a typo (use the templates).
2. Fork, create a branch: `git checkout -b glossary/add-attention-terms`.
3. Run the checks locally:
   ```bash
   pip install -e ".[dev]"
   ruff check .
   pytest
   ```
4. Open a pull request and fill in the template.

## Style rules

- **Uzbek text is Latin script only.** Use one canonical character for o' / g' (U+02BB) and for the
  tutuq belgisi (U+02BC); `uzling.normalize_uz` does this for you.
- A term is spelled the same way everywhere; check `glossary/glossary_en_uz.csv` first.
- Notebooks must run top-to-bottom on free Colab in under 20 minutes, with a fixed random seed.
  Clear outputs of very large cells before committing.
- New data must come with its source, licence and collection method in `data/DATA_SOURCES.md`.
  Never commit personal data (names, phone numbers, addresses) of real people.

## Glossary changes

Each row in `glossary/glossary_en_uz.csv` has a `status` column: `proposed` → `reviewed` → `approved`.
New terms enter as `proposed`; a linguist reviewer moves them forward.
