import pytest

from uzling import apostrophe_profile, normalize_uz, script_of, to_ascii_apostrophe
from uzling.normalize import APOSTROPHE_VARIANTS, OKINA, TUTUQ

K, T = OKINA, TUTUQ
VARIANTS = ["'", "‘", "’", "`", OKINA, TUTUQ]


@pytest.mark.parametrize("variant", VARIANTS)
def test_okina_variants_unify(variant):
    assert normalize_uz(f"o{variant}zbek") == f"o{K}zbek"
    assert normalize_uz(f"O{variant}zbekiston") == f"O{K}zbekiston"
    assert normalize_uz(f"G{variant}afur") == f"G{K}afur"
    assert normalize_uz(f"bog{variant}") == f"bog{K}"


@pytest.mark.parametrize("variant", VARIANTS)
def test_tutuq_variants_unify(variant):
    assert normalize_uz(f"ma{variant}no") == f"ma{T}no"


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("O'zbekiston", f"O{K}zbekiston"),
        ("G'afur", f"G{K}afur"),
        ("to'g'ri", f"to{K}g{K}ri"),
        ("ma'no", f"ma{T}no"),
        ("san'at", f"san{T}at"),
        ("ta'lim", f"ta{T}lim"),
        ("mo''jiza", f"mo{K}{T}jiza"),
        ("mo‘’jiza", f"mo{K}{T}jiza"),
        ("O'ZBEK", f"O{K}ZBEK"),
        (f"O{K}ZBEK", f"O{K}ZBEK"),
        ("O'ZBEKISTON", f"O{K}ZBEKISTON"),
        ("TO'G'RI", f"TO{K}G{K}RI"),
        ("tog'", f"tog{K}"),
        ("go'sht", f"go{K}sht"),
        ("g'o'za", f"g{K}o{K}za"),
        ("aʻlo", f"a{T}lo"),  # okina typed where the tutuq belongs
    ],
)
def test_required_cases(raw, expected):
    assert normalize_uz(raw) == expected


@pytest.mark.parametrize("word", ["kitob", "Toshkent", "maktablarimizda", "dollar", ""])
def test_words_without_apostrophes_unchanged(word):
    assert normalize_uz(word) == word


def test_full_sentence_with_mixed_variants():
    raw = "O`zbekiston ta’limida mo''jiza yo‘q, lekin san'at va g'oyalar to'g`ri yo'lda."
    expected = (
        f"O{K}zbekiston ta{T}limida mo{K}{T}jiza yo{K}q, lekin san{T}at va "
        f"g{K}oyalar to{K}g{K}ri yo{K}lda."
    )
    assert normalize_uz(raw) == expected


def test_quotes_left_alone():
    assert normalize_uz("U 'salom' dedi.") == "U 'salom' dedi."
    assert normalize_uz("‘Radio’ eshitdi") == "‘Radio’ eshitdi"
    assert normalize_uz("1990'lar") == "1990'lar"


def test_idempotent():
    s = "O'zbekiston ma'no mo''jiza tog' G'AFUR"
    once = normalize_uz(s)
    assert normalize_uz(once) == once


def test_only_canonical_marks_remain_in_words():
    out = normalize_uz("o'zbek ma`no to‘g’ri")
    assert set(out) & set(APOSTROPHE_VARIANTS) <= {OKINA, TUTUQ}


def test_nfc():
    decomposed = "ó"  # o + combining acute
    assert normalize_uz(decomposed) == "ó"


def test_four_spellings_become_one():
    spellings = ["o'zbek", "oʻzbek", "o‘zbek", "o`zbek"]
    assert len({normalize_uz(s) for s in spellings}) == 1


def test_ascii_and_profile():
    assert to_ascii_apostrophe("o‘zbek maʼno") == "o'zbek ma'no"
    assert apostrophe_profile("o'g`") == {"U+0027": 1, "U+0060": 1}


@pytest.mark.parametrize(
    "text,expected",
    [
        ("Oʻzbekiston poytaxti", "latin"),
        ("Ўзбекистон пойтахти", "cyrillic"),
        ("Bugun встреча bor", "mixed"),
        ("2024 — 15%", "unknown"),
        ("", "unknown"),
    ],
)
def test_script_of(text, expected):
    assert script_of(text) == expected


def test_script_of_tolerance():
    text = "Toshkent shahri juda katta va chiroyli (рус. Ташкент)"
    assert script_of(text) == "mixed"
    assert script_of(text, tolerance=0.25) == "latin"
