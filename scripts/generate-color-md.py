# Create markdown table for all color-ramps

from pathlib import Path
import pkgutil
from typing import List

from hdc.colors.hazards import __all__ as hazards_ramps
from hdc.colors.rainfall import __all__ as rainfall_ramps
from hdc.colors.temperature import __all__ as temperature_ramps
from hdc.colors.types import ColorRampElement
from hdc.colors.vegetation import __all__ as vegetation_ramps


def gen_color_table(entries: List[ColorRampElement]):
    """Generates HTML table with color ramp"""
    html_table = "<table border='1'><tr><th>Value</th><th>Color</th><th>Label</th></tr>"
    for entry in entries:
        icon_url = f"https://via.placeholder.com/15/{entry['color'].strip('#')}/000000.png?text=+"
        html_table += f"<tr><td>{entry['value']}</td><td><img src='{icon_url}' alt='color icon'/> {entry['color']}</td><td>{entry['label']}</td></tr>"

    return html_table + "</table>"


def main():
    md = """<h1>Color Ramps</h1>"""

    # Rainfall ramps

    md += "<h2>Rainfall</h2>"
    for ramp in rainfall_ramps:
        md += (
            f"<b>{ramp}</b>"
            + gen_color_table(pkgutil.resolve_name("hdc.colors:rainfall." + ramp).ramp)
            + "  "
        )

    # Vegetation ramps
    md += "<h2>Vegetation</h2>"

    for ramp in vegetation_ramps:
        md += (
            f"<b>{ramp}</b>"
            + gen_color_table(
                pkgutil.resolve_name("hdc.colors:vegetation." + ramp).ramp
            )
            + "  "
        )

    # Temperature ramps
    md += "<h2>Temperature</h2>"
    for ramp in temperature_ramps:
        md += (
            f"<b>{ramp}</b>"
            + gen_color_table(
                pkgutil.resolve_name("hdc.colors:temperature." + ramp).ramp
            )
            + "  "
        )

    # Hazards ramps
    md += "<h2>Hazards</h2>"
    for ramp in hazards_ramps:
        md += (
            f"<b>{ramp}</b>"
            + gen_color_table(pkgutil.resolve_name("hdc.colors:hazards." + ramp).ramp)
            + "  "
        )

    with open(Path(__file__).parents[1] / "color_ramps.md", "w") as f:
        f.write(md)


if __name__ == "__main__":
    main()
