"""Visualization stuff for UI"""
from rich.table import Table
from rich.text import Text
from rich.style import Style

from ._classes import HDCDiscreteRamp


def create_table(name: str, color_ramp: HDCDiscreteRamp) -> Table:
    """Create Rich table for colorramp"""
    title = Text(name, style=Style(color="deep_pink3", bold=True, italic=True))
    table = Table(show_header=True, header_style="bold orange_red1", title=title)

    table.add_column("Value")
    table.add_column("Color")
    table.add_column("Label")

    for entry in color_ramp.ramp:
        value, color, label = entry.values()
        assert color.startswith("#")
        bg_style = Style(color="black", bgcolor=color)
        table.add_row(str(value), Text("", style=bg_style), label)

    return table
