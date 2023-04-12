"""HDC colors containers"""
from typing import List

from .types import ColorRampElement, RampInput
from .utils import lagiter


class HDCBaseClass:
    """Parent class for HDC color classes"""

    def __init__(
        self,
        ramp_input: RampInput,
    ):
        if not self._validate_input(ramp_input):
            raise ValueError(
                "Number of colors must have equal number of values and labels (if provided)!"
            )
        values, colors, *labels = zip(*ramp_input)
        if labels:
            (labels,) = labels

        assert len(values) == len(colors)
        self.n = len(values)
        if labels:
            assert len(labels) == self.n

        self.vals = values
        self.cols = colors
        self.labels = labels

    @staticmethod
    def _validate_input(list_in: RampInput) -> bool:
        """Checks if tuples in List have all same length"""
        xx = [len(x) for x in list_in]
        return xx.count(xx[0]) == len(xx)


class HDCDiscreteRamp(HDCBaseClass):
    """Discrete HDC color ramp"""

    @property
    def ramp(self) -> List[ColorRampElement]:
        """returns list with dictionaries containing
            {"value": value, "color": color} or
            {"value": value, "color": color, "label": label} if
        labels are provided."""

        if self.labels:
            return [
                {"value": v, "color": c, "label": l}
                for v, c, l in zip(self.vals, self.cols, self.labels)
            ]
        return [{"value": v, "color": c} for v, c in zip(self.vals, self.cols)]

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
