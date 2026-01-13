"""Color ramps for hazards related data."""

from typing import cast

from ._classes import HDCDiscreteRamp
from .types import RampInput

__all__ = [
    "w6dfwt",
    "wai",
]

### w6d encoded flood wetland/trend
w6dfwt = HDCDiscreteRamp(
    cast(
        RampInput,
        [
            (0, "#000000", "0"),
            (1, "#0f02a7", "1"),
            (3, "#2429f4", "3"),
            (7, "#2d6bfd", "7"),
            (15, "#36a3fd", "15"),
            (31, "#2cd8fa", "31"),
            (32, "#580100", "32"),
            (48, "#9d0400", "48"),
            (56, "#e60f00", "56"),
            (60, "#fc7600", "60"),
            (62, "#ffbe00", "62"),
            (63, "#ffffff", "63"),
            (101, "#393939", "101"),
            (102, "#5a5a5a", "102"),
            (103, "#7d7d7d", "103"),
            (104, "#a2a2a2", "104"),
            (105, "#c8c8c8", "105"),
        ],
    )
)


### WAI - Water Availability Index
wai = HDCDiscreteRamp(
    cast(
        RampInput,
        [
            (1000, "#4d0000", "0.0 - 0.1"),
            (2000, "#990000", "0.1 - 0.2"),
            (3000, "#ff4500", "0.2 - 0.3"),
            (4000, "#ff8c00", "0.3 - 0.4"),
            (5000, "#ffd700", "0.4 - 0.5"),
            (6000, "#ffff99", "0.5 - 0.6"),
            (7000, "#66ccff", "0.6 - 0.7"),
            (8000, "#3399ff", "0.7 - 0.8"),
            (9000, "#0066cc", "0.8 - 0.9"),
            (10000, "#003d7a", "0.9 - 1.0"),
        ],
    )
)
