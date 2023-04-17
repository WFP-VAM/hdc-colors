"""Pytest test configs"""
import pytest


@pytest.fixture
def class_input():
    """Test input for color classes"""
    return [(1, "#FF0000", "foo"), (2, "#00FF00", "bar"), (3, "#0000FF", "biz")]
