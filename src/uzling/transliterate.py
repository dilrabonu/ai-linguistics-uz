"""Uzbek Cyrillic -> Latin transliteration (1995 Latin alphabet, rule-based).

Cyrillic characters are written as ``\\u`` escapes so that the source stays pure ASCII.
The converter handles the context-dependent letters:

* E/e at the start of a word or after a vowel -> "ye", otherwise "e"
* Ts/ts (U+0426/U+0446) -> "ts" by default; both "ts" and "s" occur in practice,
  so the output is configurable via ``ts=``
* the hard sign (U+044A) -> tutuq belgisi, the soft sign (U+044C) -> dropped
"""

from __future__ import annotations

from .normalize import OKINA, TUTUQ

_LOWER = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d",
    "ё": "yo", "ж": "j", "з": "z", "и": "i", "й": "y",
    "к": "k", "л": "l", "м": "m", "н": "n", "о": "o",
    "п": "p", "р": "r", "с": "s", "т": "t", "у": "u",
    "ф": "f", "х": "x", "ч": "ch", "ш": "sh", "щ": "sh",
    "ы": "i", "э": "e", "ю": "yu", "я": "ya",
    "ў": "o" + OKINA,   # short u  -> o'
    "қ": "q",           # qa
    "ғ": "g" + OKINA,   # ghayn -> g'
    "ҳ": "h",           # ha with descender
    "ъ": TUTUQ,         # hard sign
    "ь": "",            # soft sign
}
_E_LOWER = "е"
_TS_LOWER = "ц"
_VOWELS = set("аеёиоуэюяў")


def _is_upper(ch: str) -> bool:
    return ch != ch.lower()


def _apply_case(src: str, out: str, next_upper: bool) -> str:
    if not out or not _is_upper(src):
        return out
    # "SH" in an all-caps word, "Sh" in a capitalised word
    return out.upper() if next_upper else out[0].upper() + out[1:]


def cyr_to_lat(text: str, ts: str = "ts") -> str:
    """Transliterate Uzbek Cyrillic ``text`` to Latin script.

    >>> cyr_to_lat("\\u0422\\u043e\\u0448\\u043a\\u0435\\u043d\\u0442")
    'Toshkent'
    """
    out: list[str] = []
    for i, ch in enumerate(text):
        low = ch.lower()
        prev = text[i - 1].lower() if i > 0 else ""
        nxt = text[i + 1] if i + 1 < len(text) else ""
        next_upper = bool(nxt) and _is_upper(nxt)
        if low == _E_LOWER:
            lat = "ye" if (not prev or not prev.isalpha() or prev in _VOWELS) else "e"
        elif low == _TS_LOWER:
            lat = ts
        elif low in _LOWER:
            lat = _LOWER[low]
        else:
            out.append(ch)
            continue
        out.append(_apply_case(ch, lat, next_upper))
    return "".join(out)
