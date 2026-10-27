"""Calibration metrics for classifiers and multiple-choice LLM evaluation.

All functions take ``confidence`` (probability of the predicted answer, in [0, 1])
and ``correct`` (1 if the prediction was right, else 0).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class ReliabilityBin:
    lower: float
    upper: float
    count: int
    mean_confidence: float
    accuracy: float


def _check(confidence, correct) -> tuple[np.ndarray, np.ndarray]:
    conf = np.asarray(confidence, dtype=float)
    corr = np.asarray(correct, dtype=float)
    if conf.shape != corr.shape or conf.ndim != 1:
        raise ValueError("confidence and correct must be 1-D arrays of equal length")
    if conf.size == 0:
        raise ValueError("empty input")
    if np.any((conf < 0) | (conf > 1)):
        raise ValueError("confidence must lie in [0, 1]")
    return conf, corr


def reliability_bins(confidence, correct, n_bins: int = 10) -> list[ReliabilityBin]:
    """Equal-width bins over [0, 1]; the first bin includes 0."""
    conf, corr = _check(confidence, correct)
    edges = np.linspace(0.0, 1.0, n_bins + 1)
    idx = np.clip(np.digitize(conf, edges[1:-1], right=True), 0, n_bins - 1)
    bins = []
    for b in range(n_bins):
        mask = idx == b
        n = int(mask.sum())
        bins.append(
            ReliabilityBin(
                lower=float(edges[b]),
                upper=float(edges[b + 1]),
                count=n,
                mean_confidence=float(conf[mask].mean()) if n else float("nan"),
                accuracy=float(corr[mask].mean()) if n else float("nan"),
            )
        )
    return bins


def ece(confidence, correct, n_bins: int = 10) -> float:
    """Expected Calibration Error (Guo et al., 2017)."""
    conf, _ = _check(confidence, correct)
    total = conf.size
    return float(
        sum(b.count / total * abs(b.accuracy - b.mean_confidence)
            for b in reliability_bins(confidence, correct, n_bins) if b.count)
    )


def mce(confidence, correct, n_bins: int = 10) -> float:
    """Maximum Calibration Error: the worst bin gap."""
    gaps = [abs(b.accuracy - b.mean_confidence)
            for b in reliability_bins(confidence, correct, n_bins) if b.count]
    return float(max(gaps))


def brier(confidence, correct) -> float:
    """Brier score of the predicted answer's probability (binary form)."""
    conf, corr = _check(confidence, correct)
    return float(np.mean((conf - corr) ** 2))
