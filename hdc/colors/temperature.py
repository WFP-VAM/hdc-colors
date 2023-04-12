# pylint: disable=duplicate-code
"""Color ramps for rainfall data"""
from ._classes import HDCDiscreteRamp
from .utils import INF

### LST (in scaled kelvin)

lst_42_m24_70 = HDCDiscreteRamp(
    [
        (12457.5, "#ffffff", "< -24C"),
        (12657.5, "#fafafa", "-24C - -20C"),
        (12857.5, "#f5f5f5", "-20C - -16C"),
        (13057.5, "#ebebeb", "-16C - -12C"),
        (13257.5, "#e1e1e1", "-12C - -8C"),
        (13457.5, "#c8c8c8", "-8C - -4C"),
        (13657.5, "#05284b", "-4C - 0C"),
        (13757.5, "#1d2e83", "0C - 2C"),
        (13857.5, "#24479d", "2C - 4C"),
        (13957.5, "#2166ac", "4C - 6C"),
        (14057.5, "#0564c3", "6C - 8C"),
        (14157.5, "#1d8dbe", "8C - 10C"),
        (14257.5, "#34a9c3", "10C - 12C"),
        (14357.5, "#005867", "12C - 14C"),
        (14457.5, "#378a95", "14C - 16C"),
        (14557.5, "#6c9fa4", "16C - 18C"),
        (14657.5, "#7ab2b9", "18C - 20C"),
        (14757.5, "#57bec1", "20C - 22C"),
        (14857.5, "#85cfba", "22C - 24C"),
        (14957.5, "#aee0c4", "24C - 26C"),
        (15057.5, "#bbe4b5", "26C - 28C"),
        (15157.5, "#dcf1b2", "28C - 30C"),
        (15257.5, "#e8ffde", "30C - 32C"),
        (15357.5, "#f2fabc", "32C - 34C"),
        (15457.5, "#ffffbf", "34C - 36C"),
        (15557.5, "#ffec81", "36C - 38C"),
        (15657.5, "#fed380", "38C - 40C"),
        (15757.5, "#f5af28", "40C - 42C"),
        (15857.5, "#eac98e", "42C - 44C"),
        (15957.5, "#d5a45f", "44C - 46C"),
        (16057.5, "#bf7f2f", "46C - 48C"),
        (16157.5, "#f88d52", "48C - 50C"),
        (16257.5, "#f06405", "50C - 52C"),
        (16357.5, "#de3f2e", "52C - 54C"),
        (16457.5, "#cb181d", "54C - 56C"),
        (16557.5, "#a50026", "56C - 58C"),
        (16657.5, "#ad3a00", "58C - 60C"),
        (16757.5, "#932700", "60C - 62C"),
        (16857.5, "#7a1300", "62C - 64C"),
        (16957.5, "#67000d", "64C - 66C"),
        (17157.5, "#732600", "66C - 70C"),
        (INF, "#460000", "> 70C"),
    ]
)

### LST Anomaly (in degree difference scaled)

tdd_tnd_21_m20_20 = HDCDiscreteRamp(
    [
        (-1000, "#05284b", "< -20C"),
        (-800, "#1d2e83", "-20C to -16C"),
        (-600, "#24479d", "-16C to -12C"),
        (-500, "#2166ac", "-12C to -10C"),
        (-400, "#1d8dbe", "-10C to -8C"),
        (-300, "#34a9c3", "-8C to -6C"),
        (-200, "#6cb4de", "-6C to -4C"),
        (-150, "#7ecae7", "-4C to -3C"),
        (-100, "#90e0ef", "-3C to -2C"),
        (-50, "#c3f6ff", "-2C to -1C"),
        (50, "#fafafa", "-1C to +1C"),
        (100, "#fddbc7", "+1C to +2C"),
        (150, "#fcbba1", "+2C to +3C"),
        (200, "#fc9272", "+3C to +4C"),
        (300, "#fb6a4a", "+4C to +6C"),
        (400, "#ef3b2c", "+6C to +8C"),
        (500, "#d73027", "+8C to +10C"),
        (600, "#cb181d", "+10C to +12C"),
        (800, "#b2182b", "+12C to +16C"),
        (1000, "#a50026", "+16C to +20C"),
        (INF, "#67000d", "> +20C"),
    ]
)

tdd_tnd_21_m12_12 = HDCDiscreteRamp(
    [
        (-600, "#05284b", "< -12C"),
        (-500, "#1d2e83", "-12C to -10C"),
        (-400, "#24479d", "-10C to -8C"),
        (-350, "#2166ac", "-8C to -7C"),
        (-300, "#1d8dbe", "-7C to -6C"),
        (-250, "#34a9c3", "-6C to -5C"),
        (-200, "#6cb4de", "-5C to -4C"),
        (-150, "#7ecae7", "-4C to -3C"),
        (-100, "#90e0ef", "-3C to -2C"),
        (-50, "#c3f6ff", "-2C to -1C"),
        (50, "#fafafa", "-1C to +1C"),
        (100, "#fddbc7", "+1C to +2C"),
        (150, "#fcbba1", "+2C to +3C"),
        (200, "#fc9272", "+3C to +4C"),
        (250, "#fb6a4a", "+4C to +5C"),
        (300, "#ef3b2c", "+5C to +6C"),
        (350, "#d73027", "+6C to +7C"),
        (400, "#cb181d", "+7C to +8C"),
        (500, "#b2182b", "+8C to +10C"),
        (600, "#a50026", "+10C to +12C"),
        (INF, "#67000d", "> +12C"),
    ]
)


### LST Amplitude (diurnal temperature difference) in degrees difference scaled

taa_21_1_48 = HDCDiscreteRamp(
    [
        (50, "#05284b", "< 1C"),
        (100, "#0031ac", "1C to 2C"),
        (150, "#0564c3", "2C to 3C"),
        (200, "#1d8dbe", "3C to 4C"),
        (250, "#57bec1", "4C to 5C"),
        (300, "#004231", "5C to 6C"),
        (400, "#006b52", "6C to 8C"),
        (500, "#64a77e", "8C to 10C"),
        (600, "#86cb66", "10C to 12C"),
        (700, "#ccea83", "12C to 14C"),
        (800, "#dcf1b2", "14C to 16C"),
        (900, "#ffffbf", "16C to 18C"),
        (1000, "#ffeebd", "18C to 20C"),
        (1200, "#ffec81", "20C to 24C"),
        (1400, "#fed380", "24C to 28C"),
        (1600, "#fec754", "28C to 32C"),
        (1800, "#f5af28", "32C to 36C"),
        (2000, "#d79b0b", "36C to 40C"),
        (2200, "#d5a45f", "40C to 44C"),
        (2400, "#bf7f2f", "44C to 48C"),
        (INF, "#aa5a00", "> +48C"),
    ]
)
