# pylint: disable=missing-function-docstring,redefined-outer-name
"""Tests for hdc.colors._classes"""
import math

import numpy as np
import pytest
from matplotlib.colors import ListedColormap

from hdc.colors import rainfall, vegetation
from hdc.colors._classes import HDCBaseClass, HDCDiscreteRamp


def test_hdc_base(class_input):
    vals, cols, labels = map(list, zip(*class_input))

    with pytest.raises(ValueError):
        _ = HDCBaseClass(
            [(vals[0], cols[0], labels[0]), (vals[1], labels[1]), (vals[2], labels[2])]
        )

    r = HDCBaseClass(class_input)
    assert r.vals == vals
    assert r.cols == cols
    assert r.labels == labels

    assert isinstance(r.cmap, ListedColormap)
    assert r.cmap.N == len(r.cols)


# pylint: disable=protected-access
@pytest.mark.parametrize(
    "xx, n",
    [
        ([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 3),
        ([(1, 2), (4, 5), (7, 8)], 2),
        ([(1, 2, 3), (7, 8)], -1),
        ([(1,), (2,), (3,)], -1),
        ([(1, 2, 3, 4), (4, 5, 6, 7)], -1),
    ],
)
def test_hdc_base_input_validation(xx, n):
    if n > 0:
        assert HDCBaseClass._validate_input(xx) == n
    else:
        with pytest.raises(ValueError):
            HDCBaseClass._validate_input(xx)


def test_hdc_discrete(class_input):
    vals, cols, _ = map(list, zip(*class_input))
    r = HDCDiscreteRamp(list(zip(vals, cols)))
    assert r.vals == vals
    assert r.cols == cols
    assert r.ramp == [
        {"value": vals[0], "color": cols[0]},
        {"value": vals[1], "color": cols[1]},
        {"value": vals[2], "color": cols[2]},
    ]

    r = HDCDiscreteRamp(class_input)
    assert r.ramp == [
        {"value": 1, "color": "#FF0000", "label": "foo"},
        {"value": 2, "color": "#00FF00", "label": "bar"},
        {"value": 3, "color": "#0000FF", "label": "biz"},
    ]

    r = HDCDiscreteRamp(
        list(zip(list(vals) + [float("INF")], list(cols) + ["#FFFF00"]))
    )
    assert r.ramp_ows == [
        {"value": vals[0], "color": cols[0]},
        {"value": vals[1], "color": cols[1]},
        {"value": vals[1], "color": cols[1]},
        {"value": vals[2], "color": cols[2]},
        {"value": vals[2], "color": cols[2]},
        {"value": vals[2] + 1, "color": "#FFFF00"},
    ]


@pytest.mark.parametrize("cm", [rainfall.rfh_16_0_300, rainfall.rfh_16_0_4000])
def test_resample_identity(cm):
    _cm = cm.resample(cm.vals)
    assert _cm.vals == cm.vals
    assert _cm.cols == cm.cols
    assert isinstance(_cm, HDCDiscreteRamp)


def test_cm_resample():
    _inf = float("inf")
    cm = HDCDiscreteRamp(
        [(10, "#FF0000"), (20, "#00FF00"), (30, "#0000FF"), (_inf, "#FFFF00")]
    )
    edges = sorted(list(range(0, 40, 5)) + [_inf])
    assert set(edges).issuperset(cm.vals)

    _cm = cm.resample(edges)
    assert isinstance(_cm, HDCDiscreteRamp)
    assert _cm.vals == edges
    assert set(_cm.cols) == set(cm.cols)

    xx = np.arange(-1, 100, 1)
    xx = np.concatenate([xx, [float("inf")]])

    cc = cm.colorizer()(xx)
    _cc = _cm.colorizer()(xx)

    np.testing.assert_equal(_cc, cc)


def _max_edge(cmap):
    return max(x for x in cmap.vals if math.isfinite(x))


def _all_matching(mod, prefix):
    return [getattr(mod, n) for n in mod.__all__ if n.startswith(prefix)]


@pytest.mark.parametrize(
    "cmaps",
    [
        (rainfall.rfh_16_0_300, rainfall.rfh_16_0_4000),
        _all_matching(rainfall, "rfh_16"),
        _all_matching(rainfall, "rfq_16"),
        [],
        [vegetation.vim_14_01_09],
    ],
)
def test_unify(cmaps):
    _cmaps = HDCDiscreteRamp.unify(cmaps)
    assert len(_cmaps) == len(cmaps)

    if len(cmaps) == 0:
        return

    vmax = max(_max_edge(c) for c in cmaps)
    assert math.isfinite(vmax)

    xx = np.arange(-1, vmax, 1)
    xx = np.concatenate([xx, [float("inf")]])
    for cm, _cm in zip(cmaps, _cmaps):
        cc = cm.colorizer()(xx)
        _cc = _cm.colorizer()(xx)
        np.testing.assert_equal(_cc, cc)
