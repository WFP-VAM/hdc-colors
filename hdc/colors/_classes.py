"""HDC colors containers"""

import functools
from typing import Callable, List, Optional, Tuple, cast

import numpy as np
from matplotlib.colors import ListedColormap

from .types import ColorRampElement, NodataType, RampInput, RampInput3
from .utils import create_color_table, hex_to_rgb, lagiter


class HDCBaseClass:
    """Parent class for HDC color classes"""

    def __init__(
        self,
        ramp_input: RampInput,
    ):
        tuple_sz = self._validate_input(ramp_input)  # raises ValueError

        values = [v for v, *_ in ramp_input]
        colors = [c for _, c, *_ in ramp_input]
        labels = (
            None
            if tuple_sz != 3
            else [lbl for _, _, lbl in cast(RampInput3, ramp_input)]
        )

        self.n = len(values)
        self.vals = values
        self.cols = colors
        self.labels = labels

    @staticmethod
    def _validate_input(list_in: RampInput) -> int:
        """Checks if tuples in List have all same length"""
        xx = set(len(x) for x in list_in)
        if len(xx) != 1:
            raise ValueError("Must supply labels for all values or not at all!")
        (n,) = xx
        if n not in (2, 3):
            raise ValueError(
                "Expect data in [(value, color), ...] or [(value, color, label), ...] format"
            )
        return n

    @property
    def cmap(self) -> ListedColormap:
        """ramp colors as matplotlib listed colormap"""
        return ListedColormap([hex_to_rgb(x, True) for x in self.cols], "")

    def _repr_png_(self):
        # pylint: disable=protected-access
        return self.cmap._repr_png_()

    def _extract_palette(
        self, out_of_range_color: str = "#00000000"
    ) -> Tuple[np.ndarray, np.ndarray]:
        palette = np.asarray(
            [hex_to_rgb((c + "ff")[:9]) for c in [*self.cols, out_of_range_color]],
            dtype="uint8",
        )
        bins = np.asarray(self.vals)
        return palette, bins

    def colorizer(
        self,
        out_of_range_color: str = "#00000000",
    ) -> Callable[[np.ndarray], np.ndarray]:
        """Create colorizer operator.

        Maps single channel images to rgba according to colormap.
        """
        palette, bins = self._extract_palette(out_of_range_color)
        return functools.partial(_apply_palette, palette, bins)

    def palettizer(
        self,
        out_of_range_color: str = "#00000000",
    ) -> Tuple[Callable[[np.ndarray], np.ndarray], np.ndarray]:
        """Create colorizer operator.

        Maps single channel images to palette indexes.
        """
        palette, bins = self._extract_palette(out_of_range_color)
        return functools.partial(_digitize, bins, dtype=np.uint8), palette


class HDCDiscreteRamp(HDCBaseClass):
    """Discrete HDC color ramp"""

    @property
    def ramp(self) -> List[ColorRampElement]:
        """returns list with dictionaries containing
            {"value": value, "color": color} or
            {"value": value, "color": color, "label": label} if
        labels are provided."""

        if self.labels is None:
            return [{"value": v, "color": c} for v, c in zip(self.vals, self.cols)]
        return [
            {"value": v, "color": c, "label": l}
            for v, c, l in zip(self.vals, self.cols, self.labels)
        ]

    @property
    def ramp_ows(self):
        """returns OWS compliant color ramp"""
        ramp = []
        for prev, item in lagiter(zip(self.vals, self.cols)):
            v, c = item

            if prev is None:
                ramp.append({"value": v, "color": c})
                continue

            vp, _ = prev

            if v == float("INF"):
                ramp.append({"value": vp + 1, "color": c})
                break

            ramp.extend([{"value": vp + 1, "color": c}, {"value": v, "color": c}])
        return ramp

    def to_txt(
        self, filename: Optional[str] = None, nodata: Optional[NodataType] = None
    ):
        """Create gdal compliant color table"""
        return create_color_table(self, nodata=nodata, filename=filename)


def _apply_palette(palette, bins, x, nodata=None):
    return palette[_digitize(bins, x, dtype="int32", nodata=nodata)]


def _digitize(bins, x, dtype="uint8", nodata=None):
    binned = np.digitize(x, bins).astype(dtype)
    if nodata is not None:
        binned[x == nodata] = len(bins)
    return binned
