# pylint: disable=missing-function-docstring,redefined-outer-name
"""Tests for hdc.colors.utils"""
from pathlib import Path
from tempfile import TemporaryDirectory

import numpy as np
import pytest

from hdc.colors._classes import HDCDiscreteRamp
from hdc.colors.utils import create_color_table, hex_to_rgb, lagiter, rgb_to_hex


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
    "hex_val, rgb_val, norm",
    [
        ("#fafafa", (250, 250, 250), False),
        ("#fafafa10", (250, 250, 250, 0x10), False),
        ("#ff0000", (255, 0, 0), False),
        ("#000000", (0, 0, 0), False),
        ("#fafafa", (0.9803921568627451, 0.9803921568627451, 0.9803921568627451), True),
        (
            "#fafafaff",
            (0.9803921568627451, 0.9803921568627451, 0.9803921568627451, 1),
            True,
        ),
        ("#ff0000", (1.0, 0.0, 0.0), True),
    ],
)
def test_hex_to_rgb(hex_val, rgb_val, norm):
    assert hex_to_rgb(hex_val, norm) == rgb_val
    assert rgb_to_hex(rgb_val, norm) == hex_val


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


@pytest.mark.parametrize(
    "cm",
    [
        HDCDiscreteRamp(
            [
                (0.000, "#ff1100"),
                (10.00, "#ff2201"),
                (211.0, "#ff3302"),
                (300.0, "#ff4403"),
            ]
        )
    ],
)
@pytest.mark.parametrize("out_of_range_color", ["#ffffff00", "#00000000"])
def test_colorizer(cm: HDCDiscreteRamp, out_of_range_color: str):
    colorize = cm.colorizer(out_of_range_color=out_of_range_color)
    x = np.asarray(cm.vals)

    def to_hex(xx):
        return "#" + "".join(f"{x:02x}" for x in xx)

    hex_palette = (
        [out_of_range_color] + [c + "ff" for c in cm.cols] + [out_of_range_color]
    )

    hex_plte_native = hex_palette[1:-1]

    rgba = colorize(x - 0.1)
    assert rgba.shape == (*x.shape, 4)
    assert rgba.dtype == "uint8"
    for i in range(len(cm.vals)):
        assert to_hex(rgba[i]) == (cm.cols[i] + "ff")[:9]

    rgba = colorize(x)
    assert rgba.shape == (*x.shape, 4)
    assert rgba.dtype == "uint8"

    for i, v in enumerate(cm.vals[:-1]):
        x = np.asarray([v - 0.1, v, v + 0.1])
        yy = [to_hex(c) for c in colorize(x)]
        assert yy == [
            hex_plte_native[i],
            hex_plte_native[i],
            hex_plte_native[i + 1],
        ]


@pytest.mark.parametrize(
    "cm",
    [
        HDCDiscreteRamp(
            [
                (0.000, "#ff1100"),
                (10.00, "#ff2201"),
                (211.0, "#ff3302"),
                (300.0, "#ff4403"),
            ]
        )
    ],
)
@pytest.mark.parametrize("out_of_range_color", ["#ffffff00", "#00000000"])
def test_palettizer(cm: HDCDiscreteRamp, out_of_range_color: str):
    to_bins, pallette = cm.palettizer(out_of_range_color=out_of_range_color)
    assert len(pallette) - len(cm.cols) in (1, 2)
    assert tuple(pallette[0]) == hex_to_rgb(out_of_range_color)

    x = np.asarray([*cm.vals, cm.vals[0] - 100])

    ii = to_bins(x)
    assert ii.shape == x.shape
    assert ii.dtype == "uint8"

    for i, v in enumerate(cm.vals):
        x = np.asarray([v - 0.1, v, v + 0.1])
        # +1 because of out_of_range_color
        assert tuple(to_bins(x).tolist()) == (i + 1, i + 1, i + 2)
