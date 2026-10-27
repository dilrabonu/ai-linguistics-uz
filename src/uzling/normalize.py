"""Uzbek Latin text normalization.

Uzbek Latin script uses two different apostrophe-like marks:

* the *turned comma* in the letters oʻ and gʻ -> canonical U+02BB
  (MODIFIER LETTER TURNED COMMA)
* the *tutuq belgisi* (glottal stop), as in maʼno, sanʼat, taʼlim -> canonical U+02BC
  (MODIFIER LETTER APOSTROPHE)

On the web the same word is typed with many different characters
(ASCII ', `, U+2018, U+2019, U+02BB, U+02BC ...). For a language model these are
different byte sequences and different tokens. ``normalize_uz`` maps them all to
the canonical form, choosing ʻ or ʼ from the context.

Changes with respect to the draft ``normalize_uz`` in the book prospectus (§2)
-------------------------------------------------------------------------------
The draft replaced every mark after o/g with a single target character and left
all other marks untouched. That has three problems:

1. The tutuq belgisi (maʼno) was never normalized, so ``ma'no``, ``ma’no`` and
   ``maʼno`` stayed three different strings.
2. U+02BC was not in the list of input variants, so ``oʼzbek`` (a common error:
   the tutuq character used for oʻ) was not repaired.
3. Mapping *both* marks to one character would merge two different signs of the
   alphabet. Here the mark is chosen by context instead:

   * after o/O, when a letter follows      -> ʻ   (Oʻzbekiston, OʻZBEK)
   * after g/G, also at the end of a word  -> ʻ   (Gʻafur, togʻ)
   * between two letters otherwise         -> ʼ   (maʼno, sanʼat, moʻʼjiza)
   * anything else (quotation marks around words, 1990'lar) is left unchanged.

Known limitation: a quoted word that ends in *g* (``'bog'``) gets ʻ on its closing
quote, which is usually the right reading for Uzbek but wrong for, e.g., an English
word in quotes.
"""

from __future__ import annotations

import re
import unicodedata

#: Characters people use in place of the Uzbek apostrophe marks.
APOSTROPHE_VARIANTS: tuple[str, ...] = (
    "'",  # U+0027 APOSTROPHE
    "`",  # U+0060 GRAVE ACCENT
    "´",  # ACUTE ACCENT
    "‘",  # LEFT SINGLE QUOTATION MARK
    "’",  # RIGHT SINGLE QUOTATION MARK
    "ʻ",  # MODIFIER LETTER TURNED COMMA
    "ʼ",  # MODIFIER LETTER APOSTROPHE
    "ʹ",  # MODIFIER LETTER PRIME
)

OKINA = "ʻ"  # oʻ gʻ
TUTUQ = "ʼ"  # maʼno

_V = "[" + re.escape("".join(APOSTROPHE_VARIANTS)) + "]"
# A "letter" here: any Unicode word character that is not a digit or underscore.
# ʻ and ʼ themselves are letters (category Lm), which makes moʻʼjiza work.
_LETTER = r"[^\W\d_]"
# oʻ only when a letter (or a second mark, as in moʻʼjiza) follows: a quote closing a
# word that ends in "o" stays a quote.
_O_PATTERN = re.compile(r"([oO])" + _V + r"(?=" + _V + r"?" + _LETTER + r")")
# gʻ also at the end of a word (togʻ, bogʻ).
_G_PATTERN = re.compile(r"([gG])" + _V)
_TUTUQ_PATTERN = re.compile(r"(?<=" + _LETTER + r")" + _V + r"(?=" + _LETTER + r")")


def normalize_uz(
    text: str,
    okina: str = OKINA,
    tutuq: str = TUTUQ,
    unicode_form: str = "NFC",
) -> str:
    """Return ``text`` with Uzbek apostrophe marks unified (see module docstring).

    >>> normalize_uz("O`zbekiston") == "O\\u02bbzbekiston"
    True
    >>> normalize_uz("ma'no") == "ma\\u02bcno"
    True
    >>> normalize_uz("mo''jiza") == "mo\\u02bb\\u02bcjiza"
    True
    """
    text = unicodedata.normalize(unicode_form, text)
    text = _O_PATTERN.sub(lambda m: m.group(1) + okina, text)
    text = _G_PATTERN.sub(lambda m: m.group(1) + okina, text)
    # The oʻ/gʻ marks set above sit between letters too; keep them, make the rest ʼ.
    text = _TUTUQ_PATTERN.sub(
        lambda m: m.group(0) if m.string[m.start() - 1] in "oOgG" else tutuq, text
    )
    return text


def to_ascii_apostrophe(text: str) -> str:
    """Map every apostrophe-like mark to ASCII ``'`` (useful for search and keyboards)."""
    return re.sub(_V, "'", text)


def apostrophe_profile(text: str) -> dict[str, int]:
    """Count which apostrophe characters occur in ``text`` (keyed by U+XXXX code)."""
    counts: dict[str, int] = {}
    for ch in text:
        if ch in APOSTROPHE_VARIANTS:
            key = f"U+{ord(ch):04X}"
            counts[key] = counts.get(key, 0) + 1
    return counts


def script_shares(text: str) -> dict[str, float]:
    """Share of Latin and Cyrillic letters among the letters of ``text``.

    Only letters whose Unicode name starts with LATIN or CYRILLIC are counted, so
    digits, punctuation and the modifier letters ʻ/ʼ do not change the result.

    >>> script_shares("Toshkent")
    {'latin': 1.0, 'cyrillic': 0.0}
    """
    latin = cyrillic = 0
    for ch in text:
        if not ch.isalpha():
            continue
        name = unicodedata.name(ch, "")
        if name.startswith("LATIN"):
            latin += 1
        elif name.startswith("CYRILLIC"):
            cyrillic += 1
    total = latin + cyrillic
    if total == 0:
        return {"latin": 0.0, "cyrillic": 0.0}
    return {"latin": latin / total, "cyrillic": cyrillic / total}


def script_of(text: str, tolerance: float = 0.0) -> str:
    """Return ``"latin"``, ``"cyrillic"`` or ``"mixed"`` for ``text``.

    ``tolerance`` is the largest share of the minority script that is still ignored
    (0.0 = any mixture is "mixed"; 0.05 lets a short Russian quotation through).
    Text without Latin or Cyrillic letters returns ``"unknown"``.

    >>> script_of("Oʻzbekiston"), script_of("Ўзбекистон"), script_of("Bugun встреча bor")
    ('latin', 'cyrillic', 'mixed')
    """
    shares = script_shares(text)
    if shares["latin"] == 0.0 and shares["cyrillic"] == 0.0:
        return "unknown"
    if shares["cyrillic"] <= tolerance:
        return "latin"
    if shares["latin"] <= tolerance:
        return "cyrillic"
    return "mixed"
