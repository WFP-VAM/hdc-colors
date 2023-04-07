"""HDC colors containers"""
from typing import List, Optional, Union

from .types import ColorRampElement
from .utils import lagiter


class HDCBaseClass:
    """Parent class for HDC color classes"""

    def __init__(
        self,
        values: List[Union[int, float]],
        colors: List[str],
        labels: Optional[List[str]] = None,
    ):
        if len(values) != len(colors):
            raise ValueError("Number of colors must have equal number of values!")

        self.n = len(values)
        if (labels is not None) and (len(labels) != self.n):
            raise ValueError("Provided lables must have equal number of values!")

        self.vals = values
        self.cols = colors
        self.labels = labels


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
