# pylint: disable=missing-function-docstring,redefined-outer-name
"""Tests for hdc.colors._classes"""
import pytest

from hdc.colors._classes import HDCBaseClass, HDCDiscreteRamp


@pytest.fixture
def class_input():
    return [(1, "red", "foo"), (2, "green", "bar"), (3, "blue", "biz")]


def test_hdc_base(class_input):
    vals, cols, labels = zip(*class_input)

    with pytest.raises(ValueError):
        _ = HDCBaseClass(
            [(vals[0], cols[0], labels[0]), (vals[1], labels[1]), (vals[2], labels[2])]
        )

    r = HDCBaseClass(class_input)
    assert r.vals == vals
    assert r.cols == cols
    assert r.labels == labels


# pylint: disable=protected-access
def test_hdc_base_input_validation():
    assert HDCBaseClass._validate_input([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
    assert HDCBaseClass._validate_input([(1, 2, 3), (4,), (7, 8)]) is False
    assert HDCBaseClass._validate_input([(1, 2, 3), (4, 5, 6, 7, 8), (9,)]) is False


def test_hdc_discrete(class_input):
    vals, cols, _ = zip(*class_input)
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
        {"value": 1, "color": "red", "label": "foo"},
        {"value": 2, "color": "green", "label": "bar"},
        {"value": 3, "color": "blue", "label": "biz"},
    ]

    r = HDCDiscreteRamp(list(zip(list(vals) + [float("INF")], list(cols) + ["yellow"])))
    assert r.ramp_ows == [
        {"value": vals[0], "color": cols[0]},
        {"value": vals[1], "color": cols[1]},
        {"value": vals[1], "color": cols[1]},
        {"value": vals[2], "color": cols[2]},
        {"value": vals[2], "color": cols[2]},
        {"value": vals[2] + 1, "color": "yellow"},
    ]
