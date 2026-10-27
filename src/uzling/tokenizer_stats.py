"""Tokenizer fairness statistics: fertility and cross-lingual parity.

* fertility = tokens / whitespace words (Rust et al., 2021)
* parity    = tokens(language X) / tokens(English) on *parallel* text (Petrov et al., 2023)

The functions take any ``tokenize`` callable (e.g. ``AutoTokenizer.tokenize``),
so the module has no hard dependency on ``transformers``.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence

Tokenize = Callable[[str], Sequence[str]]


def count_tokens(tokenize: Tokenize, sentences: Sequence[str]) -> int:
    return sum(len(tokenize(s)) for s in sentences)


def fertility(tokenize: Tokenize, sentences: Sequence[str]) -> float:
    """Average number of tokens per whitespace-separated word."""
    n_words = sum(len(s.split()) for s in sentences)
    if n_words == 0:
        raise ValueError("no words in input")
    return count_tokens(tokenize, sentences) / n_words


def parity(tokenize: Tokenize, target: Sequence[str], reference: Sequence[str]) -> float:
    """Token-count ratio of ``target`` to its parallel ``reference`` (usually English).

    A parity of 2.0 means the same content costs twice as many tokens.
    """
    if len(target) != len(reference):
        raise ValueError("target and reference must be parallel (same length)")
    ref = count_tokens(tokenize, reference)
    if ref == 0:
        raise ValueError("reference has no tokens")
    return count_tokens(tokenize, target) / ref
