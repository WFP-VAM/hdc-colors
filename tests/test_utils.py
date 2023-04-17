# pylint: disable=missing-function-docstring
"""Tests for hdc.colors.utils"""
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from hdc.colors.utils import create_color_table, hex_to_rgb, lagiter
from hdc.colors._classes import HDCDiscreteRamp


def test_lagiter():
    assert list(lagiter([1, 2, 3])) == [(None, 1), (1, 2), (2, 3)]


@pytest.mark.parametrize(
    "hex_val, rgb_val",
    [("#fafafa", (250, 250, 250)), ("#ff0000", (255, 0, 0)), ("#000000", (0, 0, 0))],
)
def test_hex_to_rgb(hex_val, rgb_val):
    assert hex_to_rgb(hex_val) == rgb_val


def test_create_color_table(class_input):
    desired = "1 255 0 0\n2 0 255 0\n2 0 255 0\n3 0 0 255\n3 0 0 255\n"
    ct = HDCDiscreteRamp(class_input)
    assert create_color_table(ct) == desired

    with TemporaryDirectory() as tempdir:
        fn = tempdir + "/cols.txt"
        _ = create_color_table(ct, fn)
        fo = Path(fn)
        assert fo.exists()
        assert fo.read_text(encoding="utf-8") == desired
        fo.unlink()
        del fo

        fn = tempdir + "/cols"
        _ = create_color_table(ct, fn)
        fo = Path(fn + ".txt")
        assert fo.exists()
        assert fo.read_text(encoding="utf-8") == desired
        fo.unlink()
