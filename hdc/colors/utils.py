"""HDC colors utils"""
from itertools import tee, chain
from typing import cast, Iterable, Optional
from pathlib import Path

from .types import RGBTuple

INF = float("INF")


def lagiter(some_iterable: Iterable) -> Iterable:
    """Lagged iteration of iterable"""
    prevs, items = tee(some_iterable, 2)
    prevs = chain([None], prevs)
    return zip(prevs, items)


def hex_to_rgb(x: str) -> RGBTuple:
    "convert HEX string to RGB tuple"
    assert x.startswith("#")
    x = x.lstrip("#")
    rgb_tuple = tuple((int(x[ix : ix + 2], 16) for ix in (0, 2, 4)))
    return cast(RGBTuple, rgb_tuple)


def create_color_table(ramp, filename: Optional[str] = None) -> str:
    """Create gdal compliant color table from color ramp"""
    # pylint: disable=import-outside-toplevel
    ctable = ""

    for e in ramp.ramp_ows:
        v = e.get("value")
        c = e.get("color")
        ctable += " ".join((str(v), *map(str, hex_to_rgb(c)))) + "\n"

    if filename is not None:
        if not filename.endswith(".txt"):
            filename += ".txt"
        try:
            fobj = Path(filename)
            fobj.write_text(ctable, encoding="utf-8")
        except OSError as exc:
            print(
                f"Failed to write to {filename} - does directory exists and do you have permissions for writing?"
            )
            raise exc

    return ctable
