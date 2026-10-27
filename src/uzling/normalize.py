"""Uzbek Latin text normalization.

Uzbek Latin script uses two apostrophe-like marks:

* the *turned comma* in the letters o' and g' -> canonical U+02BB
  (MODIFIER LETTER TURNED COMMA)
* the *tutuq belgisi* (glottal stop), as in ma'no, sun'iy -> canonical U+02BC
  (MODIFIER LETTER APOSTROPHE)

On the web the same word is typed with many different characters
(ASCII ', `, U+2018, U+2019, U+02BB, U+02BC ...). For a language model these are
different byte sequences and different tokens. ``normalize_uz`` maps them all to
one canonical form.
"""

from __future__ import annotations

import re
import unicodedata

#: Characters people use in place of the Uzbek apostrophe marks.
APOSTROPHE_VARIANTS: tuple[str, ...] = (
    "'",       # U+0027 APOSTROPHE
    "`",       # U+0060 GRAVE ACCENT
    "´",  # ACUTE ACCENT
    "‘",  # LEFT SINGLE QUOTATION MARK
    "’",  # RIGHT SINGLE QUOTATION MARK
    "ʻ",  # MODIFIER LETTER TURNED COMMA
    "ʼ",  # MODIFIER LETTER APOSTROPHE
    "ʹ",  # MODIFIER LETTER PRIME
)

OKINA = "ʻ"   # o' g'
TUTUQ = "ʼ"   # ma'no

_VARIANTS_CLASS = "[" + re.escape("".join(APOSTROPHE_VARIANTS)) + "]"
# o/g followed by an apostrophe-like mark -> letter with okina
_OG_PATTERN = re.compile(r"([oOgG])" + _VARIANTS_CLASS)
# an apostrophe-like mark between two letters (not after o/g) -> tutuq belgisi
_TUTUQ_PATTERN = re.compile(r"(?<=[^\W\doOgG_])" + _VARIANTS_CLASS + r"(?=\w)")


def normalize_uz(
    text: str,
    okina: str = OKINA,
    tutuq: str = TUTUQ,
    unicode_form: str = "NFC",
) -> str:
    """Return ``text`` with Uzbek apostrophe marks unified.

    >>> normalize_uz("O`zbekiston") == "O\\u02bbzbekiston"
    True
    >>> normalize_uz("ma'no") == "ma\\u02bcno"
    True
    """
    text = unicodedata.normalize(unicode_form, text)
    text = _OG_PATTERN.sub(lambda m: m.group(1) + okina, text)
    text = _TUTUQ_PATTERN.sub(tutuq, text)
    return text


def to_ascii_apostrophe(text: str) -> str:
    """Map every apostrophe-like mark to ASCII ``'`` (useful for search and keyboards)."""
    return re.sub(_VARIANTS_CLASS, "'", text)


def apostrophe_profile(text: str) -> dict[str, int]:
    """Count which apostrophe characters occur in ``text`` (keyed by U+XXXX code)."""
    counts: dict[str, int] = {}
    for ch in text:
        if ch in APOSTROPHE_VARIANTS:
            key = f"U+{ord(ch):04X}"
            counts[key] = counts.get(key, 0) + 1
    return counts
