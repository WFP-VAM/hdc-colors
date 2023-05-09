# pylint: disable=duplicate-code
"""Color ramps for rainfall data"""
from ._classes import HDCDiscreteRamp
from .utils import INF

### Rainfall (aggregations)

__all__ = [
    "rfh_16_0_300",
    "rfh_16_0_400",
    "rfh_16_0_600",
    "rfh_16_0_800",
    "rfh_16_0_1000",
    "rfh_16_0_1600",
    "rfh_16_0_2000",
    "rfh_16_0_2400",
    "rfh_16_0_4000",
    "rfq_14_20_400",
    "ryq_14_50_200",
    "rxs",
    "xlhie_12_0_10",
    "xnhie_12_0_14",
    "dlx_13_0_26",
    "dlx_13_0_40",
]

rfh_16_0_300 = HDCDiscreteRamp(
    [
        (0, "#fafafa", "0 mm"),
        (2, "#fffadf", "1-2 mm"),
        (5, "#d3f9d0", "2-5 mm"),
        (10, "#a9e4a3", "5-10 mm"),
        (20, "#7cc594", "10-20 mm"),
        (30, "#5eab91", "20-30 mm"),
        (40, "#9fffe8", "30-40 mm"),
        (50, "#90e0ef", "40-50 mm"),
        (60, "#00b1de", "50-60 mm"),
        (80, "#0083f3", "60-80 mm"),
        (100, "#0052cd", "80-100 mm"),
        (120, "#0000c8", "100-120 mm"),
        (150, "#6003b8", "120-150 mm"),
        (200, "#a002fa", "150-200 mm"),
        (300, "#fa78fa", "200-300 mm"),
        (INF, "#ffc4ee", "> 300 mm"),
    ]
)

rfh_16_0_400 = HDCDiscreteRamp(
    [
        (0, "#fafafa", "0 mm"),
        (5, "#fffadf", "1-5 mm"),
        (10, "#d3f9d0", "5-10 mm"),
        (20, "#a9e4a3", "10-20 mm"),
        (30, "#7cc594", "20-30 mm"),
        (40, "#5eab91", "30-40 mm"),
        (60, "#9fffe8", "40-60 mm"),
        (90, "#90e0ef", "60-90 mm"),
        (120, "#00b1de", "90-120 mm"),
        (150, "#0083f3", "120-150 mm"),
        (200, "#0052cd", "150-200 mm"),
        (250, "#0000c8", "200-250 mm"),
        (300, "#6003b8", "250-300 mm"),
        (350, "#a002fa", "300-350 mm"),
        (400, "#fa78fa", "350-400 mm"),
        (INF, "#ffc4ee", "> 400 mm"),
    ]
)

rfh_16_0_600 = HDCDiscreteRamp(
    [
        (0, "#fafafa", "0 mm"),
        (5, "#fffadf", "1-5 mm"),
        (10, "#d3f9d0", "5-10 mm"),
        (20, "#a9e4a3", "10-20 mm"),
        (30, "#7cc594", "20-30 mm"),
        (50, "#5eab91", "30-50 mm"),
        (80, "#9fffe8", "50-80 mm"),
        (100, "#90e0ef", "80-100 mm"),
        (150, "#00b1de", "100-150 mm"),
        (200, "#0083f3", "150-200 mm"),
        (250, "#0052cd", "200-250 mm"),
        (300, "#0000c8", "250-300 mm"),
        (400, "#6003b8", "300-400 mm"),
        (500, "#a002fa", "400-500 mm"),
        (700, "#fa78fa", "500-700 mm"),
        (INF, "#ffc4ee", "> 700 mm"),
    ]
)

rfh_16_0_800 = HDCDiscreteRamp(
    [
        (0, "#fafafa", "0 mm"),
        (10, "#fffadf", "1-10 mm"),
        (20, "#d3f9d0", "10-20 mm"),
        (30, "#a9e4a3", "20-30 mm"),
        (50, "#7cc594", "30-50 mm"),
        (80, "#5eab91", "50-80 mm"),
        (100, "#9fffe8", "80-100 mm"),
        (150, "#90e0ef", "100-150 mm"),
        (200, "#00b1de", "150-200 mm"),
        (300, "#0083f3", "200-300 mm"),
        (400, "#0052cd", "300-400 mm"),
        (500, "#0000c8", "400-500 mm"),
        (600, "#6003b8", "500-600 mm"),
        (700, "#a002fa", "600-700 mm"),
        (800, "#fa78fa", "700-800 mm"),
        (INF, "#ffc4ee", "> 800 mm"),
    ]
)

rfh_16_0_1000 = HDCDiscreteRamp(
    [
        (0, "#fafafa", "0 mm"),
        (10, "#fffadf", "1-10 mm"),
        (20, "#d3f9d0", "10-20 mm"),
        (30, "#a9e4a3", "20-30 mm"),
        (50, "#7cc594", "30-50 mm"),
        (100, "#5eab91", "50-100 mm"),
        (200, "#9fffe8", "100-200 mm"),
        (300, "#90e0ef", "200-300 mm"),
        (400, "#00b1de", "300-400 mm"),
        (500, "#0083f3", "400-500 mm"),
        (600, "#0052cd", "500-600 mm"),
        (700, "#0000c8", "600-700 mm"),
        (800, "#6003b8", "700-800 mm"),
        (900, "#a002fa", "800-900 mm"),
        (1000, "#fa78fa", "900-1000 mm"),
        (INF, "#ffc4ee", "> 1000 mm"),
    ]
)

rfh_16_0_1600 = HDCDiscreteRamp(
    [
        (0, "#fafafa", "0 mm"),
        (10, "#fffadf", "1-10 mm"),
        (20, "#d3f9d0", "10-20 mm"),
        (50, "#a9e4a3", "20-50 mm"),
        (100, "#7cc594", "50-100 mm"),
        (200, "#5eab91", "100-200 mm"),
        (300, "#9fffe8", "200-300 mm"),
        (400, "#90e0ef", "300-400 mm"),
        (600, "#00b1de", "400-600 mm"),
        (800, "#0083f3", "600-800 mm"),
        (900, "#0052cd", "800-900 mm"),
        (1000, "#0000c8", "900-1000 mm"),
        (1200, "#6003b8", "1000-1200 mm"),
        (1400, "#a002fa", "1200-1400 mm"),
        (1600, "#fa78fa", "1400-1600 mm"),
        (INF, "#ffc4ee", "> 1600 mm"),
    ]
)


rfh_16_0_2000 = HDCDiscreteRamp(
    [
        (0, "#fafafa", "0 mm"),
        (10, "#fffadf", "1-10 mm"),
        (50, "#d3f9d0", "10-50 mm"),
        (100, "#a9e4a3", "50-100 mm"),
        (200, "#7cc594", "100-200 mm"),
        (300, "#5eab91", "200-300 mm"),
        (400, "#9fffe8", "300-400 mm"),
        (600, "#90e0ef", "400-600 mm"),
        (800, "#00b1de", "600-800 mm"),
        (1000, "#0083f3", "800-1000 mm"),
        (1200, "#0052cd", "1000-1200 mm"),
        (1400, "#0000c8", "1200-1400 mm"),
        (1600, "#6003b8", "1400-1600 mm"),
        (1800, "#a002fa", "1600-1800 mm"),
        (2000, "#fa78fa", "1800-2000 mm"),
        (INF, "#ffc4ee", "> 2000 mm"),
    ]
)

rfh_16_0_2400 = HDCDiscreteRamp(
    [
        (0, "#fafafa", "0 mm"),
        (10, "#fffadf", "1-10 mm"),
        (50, "#d3f9d0", "10-50 mm"),
        (100, "#a9e4a3", "50-100 mm"),
        (200, "#7cc594", "100-200 mm"),
        (400, "#5eab91", "200-400 mm"),
        (600, "#9fffe8", "400-600 mm"),
        (800, "#90e0ef", "600-800 mm"),
        (1000, "#00b1de", "800-1000 mm"),
        (1200, "#0083f3", "1000-1200 mm"),
        (1400, "#0052cd", "1200-1400 mm"),
        (1600, "#0000c8", "1400-1600 mm"),
        (1800, "#6003b8", "1600-1800 mm"),
        (2000, "#a002fa", "1800-2000 mm"),
        (2400, "#fa78fa", "2000-2400 mm"),
        (INF, "#ffc4ee", "> 2400 mm"),
    ]
)

rfh_16_0_4000 = HDCDiscreteRamp(
    [
        (0, "#fafafa", "0 mm"),
        (50, "#fffadf", "1-50 mm"),
        (100, "#d3f9d0", "50-100 mm"),
        (200, "#a9e4a3", "100-200 mm"),
        (300, "#7cc594", "200-300 mm"),
        (400, "#5eab91", "300-400 mm"),
        (600, "#9fffe8", "400-600 mm"),
        (800, "#90e0ef", "600-800 mm"),
        (1000, "#00b1de", "800-1000 mm"),
        (1500, "#0083f3", "1000-1500 mm"),
        (2000, "#0052cd", "1500-2000 mm"),
        (2500, "#0000c8", "2000-2500 mm"),
        (3000, "#6003b8", "2500-3000 mm"),
        (3500, "#a002fa", "3000-3500 mm"),
        (4000, "#fa78fa", "3500-4000 mm"),
        (INF, "#ffc4ee", "> 4000 mm"),
    ]
)

### Rainfall anomalies

rfq_14_20_400 = HDCDiscreteRamp(
    [
        (20, "#8c4800", "< 20%"),
        (40, "#af6b27", "20-40%"),
        (60, "#d58c3e", "40-60%"),
        (70, "#eaa83d", "60-70%"),
        (80, "#f5c878", "70-80%"),
        (90, "#fff0c4", "80-90%"),
        (110, "#fafafa", "90-110%"),
        (120, "#befafa", "110-120%"),
        (130, "#78e2f0", "120-130%"),
        (150, "#00b9de", "130-150%"),
        (200, "#0083f3", "150-200%"),
        (300, "#0052cd", "200-300%"),
        (400, "#0000c8", "300-400%"),
        (INF, "#a002fa", "> 400%"),
    ]
)

ryq_14_50_200 = HDCDiscreteRamp(
    [
        (50, "#8c4800", "< 50%"),
        (60, "#af6b27", "50-60%"),
        (70, "#d58c3e", "60-70%"),
        (80, "#eaa83d", "70-80%"),
        (90, "#f5c878", "80-90%"),
        (95, "#fff0c4", "90-95%"),
        (105, "#fafafa", "95-105%"),
        (110, "#befafa", "105-110%"),
        (120, "#78e2f0", "110-120%"),
        (130, "#00b9de", "120-130%"),
        (150, "#0083f3", "130-150%"),
        (170, "#0052cd", "150-170%"),
        (200, "#0000c8", "170-200%"),
        (INF, "#a002fa", "> 200%"),
    ]
)


### SPI (scaled by 1000)

rxs = HDCDiscreteRamp(
    [
        (-2000, "#730000", "< -2.0"),
        (-1500, "#e70001", "-1.5 to -2.0"),
        (-1200, "#ffaa01", "-1.2 to -1.5"),
        (-700, "#ffd37b", "-0.7 to -1.2"),
        (-500, "#ffff02", "-0.5 to -0.7"),
        (500, "#f0f0f0", "-0.5 to 0.5"),
        (700, "#beebff", "0.5 to 0.7"),
        (1200, "#73b2ff", "0.7 to 1.2"),
        (1500, "#0271ff", "1.2 to 1.5"),
        (2000, "#004dad", "1.5 to 2.0"),
        (INF, "#ad03e6", "> 2.0"),
    ]
)

### Daily indicators

xlhie_12_0_10 = HDCDiscreteRamp(
    [
        (0, "#fafafa", "None"),
        (1, "#d3f9d0", "1 Day"),
        (2, "#a9e4a3", "2 Days"),
        (3, "#5eab91", "3 Days"),
        (4, "#9fffe8", "4 Days"),
        (5, "#90e0ef", "5 Days"),
        (6, "#00b1de", "6 Days"),
        (7, "#0083f3", "7 Days"),
        (8, "#0052cd", "8 Days"),
        (9, "#0031ac", "9 Days"),
        (10, "#a002fa", "10 Days"),
        (INF, "#ffc4ee", "> 10 Days"),
    ]
)

xnhie_12_0_14 = HDCDiscreteRamp(
    [
        (0, "#fafafa", "None"),
        (1, "#d3f9d0", "1 Day"),
        (2, "#a9e4a3", "2 Days"),
        (3, "#5eab91", "3 Days"),
        (4, "#9fffe8", "4 Days"),
        (5, "#90e0ef", "5 Days"),
        (6, "#00b1de", "6 Days"),
        (8, "#0083f3", "7-8 Days"),
        (10, "#0052cd", "9-10 Days"),
        (12, "#0031ac", "11-12 Days"),
        (14, "#a002fa", "13-14 Days"),
        (INF, "#ffc4ee", "> 14 Days"),
    ]
)


dlx_13_0_26 = HDCDiscreteRamp(
    [
        (0, "#6c9fa4", "None"),
        (4, "#57bec1", "1-4 Days"),
        (6, "#aee0c4", "5-6 Days"),
        (8, "#dcf1b2", "7-8 Days"),
        (10, "#ffffbf", "9-10 Days"),
        (12, "#ffeebd", "11-12 Days"),
        (14, "#ffec81", "13-14 Days"),
        (16, "#fed380", "15-16 Days"),
        (18, "#fec754", "17-18 Days"),
        (20, "#f5af28", "19-20 Days"),
        (22, "#d79b0b", "21-22 Days"),
        (23, "#c98a4b", "23-26 Days"),
        (INF, "#aa5a00", "> 26 Days"),
    ]
)

dlx_13_0_40 = HDCDiscreteRamp(
    [
        (0, "#6c9fa4", "None"),
        (6, "#57bec1", "1-6 Days"),
        (9, "#aee0c4", "7-9 Days"),
        (12, "#dcf1b2", "10-12 Days"),
        (15, "#ffffbf", "13-15 Days"),
        (18, "#ffeebd", "16-18 Days"),
        (21, "#ffec81", "19-21 Days"),
        (24, "#fed380", "22-24 Days"),
        (27, "#fec754", "25-27 Days"),
        (30, "#f5af28", "28-30 Days"),
        (35, "#d79b0b", "31-35 Days"),
        (40, "#c98a4b", "36-40 Days"),
        (INF, "#aa5a00", "> 40 Days"),
    ]
)
