# pylint: disable=missing-function-docstring
"""Tests for hdc.colors.utils"""
from hdc.colors.utils import lagiter


def test_lagiter():
    assert list(lagiter([1, 2, 3])) == [(None, 1), (1, 2), (2, 3)]
