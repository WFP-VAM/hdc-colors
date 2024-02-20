"""HDC colors containers"""

import functools
import math
from typing import TYPE_CHECKING, Callable, List, Optional, Sequence, Tuple, cast

import numpy as np

from .types import ColorRampElement, NodataType, RampInput, RampInput3, SomeNumber
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
    def cmap(self) -> "matplotlib.colors.ListedColormap":
        """ramp colors as matplotlib listed colormap"""
        # pylint: disable=import-outside-toplevel
        from matplotlib.colors import ListedColormap

        return ListedColormap([hex_to_rgb(x, True) for x in self.cols], "")

    def _repr_png_(self):
        # pylint: disable=protected-access
        return self.cmap._repr_png_()

    def _extract_palette(
        self, out_of_range_color: str = "#00000000"
    ) -> Tuple[np.ndarray, np.ndarray]:
        palette = [out_of_range_color, *self.cols]

        if math.isfinite(self.vals[-1]):
            palette.append(out_of_range_color)

        bins = np.asarray([float("-inf"), *self.vals], dtype="float32")
        palette = np.asarray(
            [hex_to_rgb((c + "ff")[:9]) for c in palette], dtype="uint8"
        )
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

    def resample(self, edges: List[SomeNumber]) -> "HDCBaseClass":
        """
        Resample color ramp to new edges.

        Same colors should be produced on the output, but number of discrete
        bins changes. This is useful for computing bin-compatible color ramps
        from a set of several.

        Args:
            edges (np.ndarray): new bin edges
        """
        to_bins, _ = self.palettizer()
        _edges = np.asarray(edges)
        new_cols: List[str] = [self.cols[i - 1] for i in to_bins(_edges - 0.001)]
        return type(self)(list(zip(edges, new_cols)))

    @staticmethod
    def unify(ramps: Sequence["HDCBaseClass"]) -> List["HDCBaseClass"]:
        """Unify color ramps to common bin edges"""
        if len(ramps) == 0:
            return []
        if len(ramps) == 1:
            return [ramps[0]]

        edges = set()
        for r in ramps:
            edges.update(r.vals)
        edges = sorted(edges)
        return [r.resample(edges) for r in ramps]


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
    binned = np.digitize(x, bins, right=False).astype(dtype)
    if nodata is not None:
        binned[x == nodata] = 0
    dtype = getattr(x, "dtype", None)
    if dtype and dtype.kind == "f":
        inf_bin = len(bins) - 1 if math.isinf(bins[-1]) else 0
        binned[np.isinf(x)] = inf_bin

    return binned


if TYPE_CHECKING:
    # pylint: disable=wrong-import-position
    import matplotlib.colors
