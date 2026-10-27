"""uzling: small utilities accompanying the textbook *Sun'iy intellekt lingvistikasi*."""

from .calibration import brier, ece, mce, reliability_bins
from .normalize import apostrophe_profile, normalize_uz, script_of, to_ascii_apostrophe
from .tokenizer_stats import fertility, parity
from .transliterate import cyr_to_lat

__all__ = [
    "apostrophe_profile",
    "brier",
    "cyr_to_lat",
    "ece",
    "fertility",
    "mce",
    "normalize_uz",
    "parity",
    "reliability_bins",
    "script_of",
    "to_ascii_apostrophe",
]
__version__ = "0.1.0"
