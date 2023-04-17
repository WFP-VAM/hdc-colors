# pylint: disable=missing-function-docstring,redefined-outer-name
"""Tests for hdc.colors.utils"""
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from hdc.colors.utils import create_color_table, hex_to_rgb, lagiter
from hdc.colors._classes import HDCDiscreteRamp


@pytest.fixture
def desired():
    return """1 255 0 0
2 0 255 0
2 0 255 0
3 0 0 255
3 0 0 255
"""


@pytest.fixture
def desired_nodata():
    return """0 255 255 255 0
1 255 0 0 255
2 0 255 0 255
2 0 255 0 255
3 0 0 255 255
3 0 0 255 255
"""


def test_lagiter():
    assert list(lagiter([1, 2, 3])) == [(None, 1), (1, 2), (2, 3)]


@pytest.mark.parametrize(
    "hex_val, rgb_val",
    [("#fafafa", (250, 250, 250)), ("#ff0000", (255, 0, 0)), ("#000000", (0, 0, 0))],
)
def test_hex_to_rgb(hex_val, rgb_val):
    assert hex_to_rgb(hex_val) == rgb_val


@pytest.mark.parametrize(
    "nodata, table_out",
    [
        (None, "desired"),
        (0, "desired_nodata"),
    ],
)
def test_create_color_table(class_input, nodata, table_out, request):
    ct = HDCDiscreteRamp(class_input)
    assert create_color_table(ct, nodata=nodata) == request.getfixturevalue(table_out)


def test_create_color_table_file(class_input, desired):
    with TemporaryDirectory() as tempdir:
        ct = HDCDiscreteRamp(class_input)
        fn = tempdir + "/cols.txt"
        _ = create_color_table(ct, filename=fn)
        fo = Path(fn)
        assert fo.exists()
        assert fo.read_text(encoding="utf-8") == desired
        fo.unlink()
        del fo

        fn = tempdir + "/cols"
        _ = create_color_table(ct, filename=fn)
        fo = Path(fn + ".txt")
        assert fo.exists()
        assert fo.read_text(encoding="utf-8") == desired
        fo.unlink()
