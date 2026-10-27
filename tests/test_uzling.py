import math

import pytest

from uzling import (
    apostrophe_profile,
    brier,
    cyr_to_lat,
    ece,
    fertility,
    mce,
    normalize_uz,
    parity,
    reliability_bins,
    to_ascii_apostrophe,
)
from uzling.normalize import OKINA, TUTUQ

# ---------- normalize ----------

@pytest.mark.parametrize("variant", ["'", "`", "‘", "’", "ʻ", "ʼ"])
def test_okina_variants_unify(variant):
    assert normalize_uz(f"o{variant}zbek") == f"o{OKINA}zbek"
    assert normalize_uz(f"O{variant}zbekiston") == f"O{OKINA}zbekiston"
    assert normalize_uz(f"bog{variant}") == f"bog{OKINA}"


@pytest.mark.parametrize("word,expected", [
    ("ma'no", f"ma{TUTUQ}no"),
    ("sun`iy", f"sun{TUTUQ}iy"),
    ("ta’lim", f"ta{TUTUQ}lim"),
])
def test_tutuq(word, expected):
    assert normalize_uz(word) == expected


def test_quotes_left_alone():
    assert normalize_uz("U 'salom' dedi.") == "U 'salom' dedi."


def test_four_spellings_become_one():
    spellings = ["o'zbek", "oʻzbek", "o‘zbek", "o`zbek"]
    assert len({normalize_uz(s) for s in spellings}) == 1


def test_ascii_and_profile():
    assert to_ascii_apostrophe("o‘zbek maʼno") == "o'zbek ma'no"
    assert apostrophe_profile("o'g`") == {"U+0027": 1, "U+0060": 1}

# ---------- transliterate ----------

def test_cyr_basic():
    toshkent = "Тошкент"
    assert cyr_to_lat(toshkent) == "Toshkent"


def test_cyr_special_letters():
    ozbek = "ўзбек"          # o'zbek
    assert cyr_to_lat(ozbek) == f"o{OKINA}zbek"
    assert cyr_to_lat("ғалла") == f"g{OKINA}alla"
    assert cyr_to_lat("қалам") == "qalam"


def test_cyr_ye_rule():
    assert cyr_to_lat("ер") == "yer"                  # word-initial
    assert cyr_to_lat("кет") == "ket"            # after consonant
    assert cyr_to_lat("оилае") == "oilaye"  # after vowel


def test_cyr_digraph_case():
    assert cyr_to_lat("Шаҳар") == "Shahar"
    assert cyr_to_lat("ШАҲАР") == "SHAHAR"
    assert cyr_to_lat("Хат") == "Xat"

# ---------- tokenizer stats ----------

def _chars(s):
    return [c for c in s if not c.isspace()]


def test_fertility_and_parity():
    assert fertility(str.split, ["bir ikki uch"]) == 1.0
    assert fertility(_chars, ["ab cd"]) == 2.0
    assert parity(_chars, ["aaaa"], ["aa"]) == 2.0
    with pytest.raises(ValueError):
        parity(_chars, ["a"], ["a", "b"])

# ---------- calibration ----------

def test_perfect_calibration():
    conf = [0.0] * 10 + [1.0] * 10
    corr = [0] * 10 + [1] * 10
    assert ece(conf, corr) == pytest.approx(0.0)
    assert mce(conf, corr) == pytest.approx(0.0)
    assert brier(conf, corr) == pytest.approx(0.0)


def test_overconfident_model():
    conf = [0.9] * 10
    corr = [1] * 5 + [0] * 5
    assert ece(conf, corr) == pytest.approx(0.4)
    assert brier(conf, corr) == pytest.approx((5 * 0.01 + 5 * 0.81) / 10)


def test_bins_cover_all_points():
    conf = [0.05, 0.15, 0.95, 1.0, 0.0]
    bins = reliability_bins(conf, [1, 0, 1, 1, 0], n_bins=10)
    assert sum(b.count for b in bins) == len(conf)
    assert math.isnan(bins[5].accuracy)


def test_invalid_confidence():
    with pytest.raises(ValueError):
        ece([1.2], [1])
