# pylint: disable=missing-function-docstring
"""Tests for hdc.colors.utils"""
import pytest

from hdc.colors.utils import hex_to_rgb, lagiter


def test_lagiter():
    assert list(lagiter([1, 2, 3])) == [(None, 1), (1, 2), (2, 3)]


@pytest.mark.parametrize(
    "hex_val, rgb_val",
    [("#fafafa", (250, 250, 250)), ("#ff0000", (255, 0, 0)), ("#000000", (0, 0, 0))],
)
def test_hex_to_rgb(hex_val, rgb_val):
    assert hex_to_rgb(hex_val) == rgb_val
