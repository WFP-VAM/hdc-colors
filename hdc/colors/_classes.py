"""HDC colors containers"""
from typing import cast, List, Optional

from .types import ColorRampElement, NodataType, RampInput, RampInput3
from .utils import create_color_table, lagiter


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
        self, nodata: Optional[NodataType] = None, filename: Optional[str] = None
    ):
        """Create gdal compliant color table"""
        return create_color_table(self, nodata=nodata, filename=filename)
