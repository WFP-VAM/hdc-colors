"""HDC colors utils"""
from itertools import tee, chain
from typing import cast, Iterable, Optional
from pathlib import Path

from .types import NodataType, RGBTuple

INF = float("INF")


def lagiter(some_iterable: Iterable) -> Iterable:
    """Lagged iteration of iterable"""
    prevs, items = tee(some_iterable, 2)
    prevs = chain([None], prevs)
    return zip(prevs, items)


def hex_to_rgb(x: str, normalize: bool = False) -> RGBTuple:
    "convert HEX string to RGB tuple"

    def _maybe_norm(x):
        return x / 255 if normalize else x

    assert x.startswith("#")
    x = x.lstrip("#")
    rgb_tuple = tuple(
        _maybe_norm(int(x[ix : ix + 2], 16)) for ix in (0, 2, 4)
    )
    return cast(RGBTuple, rgb_tuple)


def create_color_table(
    ramp, nodata: Optional[NodataType] = None, filename: Optional[str] = None
) -> str:
    """Create gdal compliant color table from color ramp"""
    # initialize table with nodata or empty
    ctable = "" if nodata is None else f"{nodata} 255 255 255 0\n"

    for e in ramp.ramp_ows:
        v = e.get("value")
        c = e.get("color")

        row = [str(v), *map(str, hex_to_rgb(c))]

        if nodata is not None:
            row.append("255")
        ctable += " ".join(row) + "\n"

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
