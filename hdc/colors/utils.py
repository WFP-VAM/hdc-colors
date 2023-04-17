"""HDC colors utils"""
from itertools import tee, chain
from typing import Iterable, Tuple

INF = float("INF")


def lagiter(some_iterable: Iterable) -> Iterable:
    """Lagged iteration of iterable"""
    prevs, items = tee(some_iterable, 2)
    prevs = chain([None], prevs)
    return zip(prevs, items)


def hex_to_rgb(x: str) -> Tuple[int]:
    "convert HEX string to RGB tuple"
    assert x.startswith("#")
    x = x.lstrip("#")
    return tuple((int(x[ix : ix + 2], 16) for ix in (0, 2, 4)))
