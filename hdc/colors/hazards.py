"""Color ramps for hazards related data"""

from typing import cast
from ._classes import HDCDiscreteRamp
from .types import RampInput

__all__ = [
    "w6d_flood",
]

### w6d encoded flood trend
w6d_flood = HDCDiscreteRamp(
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
