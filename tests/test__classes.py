# pylint: disable=missing-function-docstring,redefined-outer-name
"""Tests for hdc.colors._classes"""
import pytest

from hdc.colors._classes import HDCBaseClass, HDCDiscreteRamp


@pytest.fixture
def class_input():
    return [1, 2, 3], ["red", "green", "blue"], ["foo", "bar", "biz"]


def test_hdc_base(class_input):
    vals, cols, labels = class_input
    with pytest.raises(ValueError):
        _ = HDCBaseClass(vals, cols[:1])
    with pytest.raises(ValueError):
        _ = HDCBaseClass(vals[:1], cols)

    with pytest.raises(ValueError):
        _ = HDCBaseClass(vals, cols, labels=labels[:1])

    r = HDCBaseClass(vals, cols, labels)
    assert r.vals == vals
    assert r.cols == cols
    assert r.labels == labels


def test_hdc_discrete(class_input):
    vals, cols, labels = class_input
    r = HDCDiscreteRamp(vals, cols)
    assert r.ramp == [
        {"value": vals[0], "color": cols[0]},
        {"value": vals[1], "color": cols[1]},
        {"value": vals[2], "color": cols[2]},
    ]

    r = HDCDiscreteRamp(vals, cols, labels)
    assert r.ramp == [
        {"value": 1, "color": "red", "label": "foo"},
        {"value": 2, "color": "green", "label": "bar"},
        {"value": 3, "color": "blue", "label": "biz"},
    ]

    r = HDCDiscreteRamp(vals + [float("INF")], cols + ["yellow"])
    assert r.ramp_ows == [
        {"value": vals[0], "color": cols[0]},
        {"value": vals[1], "color": cols[1]},
        {"value": vals[1], "color": cols[1]},
        {"value": vals[2], "color": cols[2]},
        {"value": vals[2], "color": cols[2]},
        {"value": vals[2] + 1, "color": "yellow"},
    ]
