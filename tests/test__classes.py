# pylint: disable=missing-function-docstring,redefined-outer-name
"""Tests for hdc.colors._classes"""
from matplotlib.colors import ListedColormap
import pytest

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
