import math

import pytest

from uzling import brier, cyr_to_lat, ece, mce, reliability_bins
from uzling.normalize import OKINA

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
