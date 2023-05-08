"""Visualization stuff for UI"""
import importlib
from typing import Iterator, List, Optional, Tuple

from rich.table import Table
from rich.text import Text
from rich.rule import Rule
from rich.style import Style

from hdc.colors._classes import HDCDiscreteRamp
from hdc.colors.rainfall import __all__ as rainfall_ramps
from hdc.colors.vegetation import __all__ as vegetation_ramps
from hdc.colors.temperature import __all__ as temperature_ramps


def _spawn_title(name, **kwargs):
    return Text(name, style=Style(**kwargs))


def create_table(name: str, color_ramp: HDCDiscreteRamp) -> Table:
    """Create Rich table for colorramp"""
    title = _spawn_title(name, color="deep_pink3", bold=True, italic=True)
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


def _table_gen(
    rel_module: str, all_ramps: List[str], ramp_filter: Optional[Tuple[str]] = None
) -> Iterator[Table]:
    mod = importlib.import_module(rel_module, "hdc.colors")
    for ramp in all_ramps:
        if ramp_filter:
            if ramp not in ramp_filter:
                continue

        table = create_table(ramp, getattr(mod, ramp))
        yield table


def create_overview_table() -> Table:
    """Create overview table for hdc.colors ramps"""

    def _hline():
        r = Rule(style=Style(color="magenta"))
        return r, r

    title = _spawn_title("HDC Color Ramps", color="deep_pink3", bold=True, italic=True)
    table = Table(show_header=True, header_style="bold orange_red1", title=title)

    table.add_column("Name")
    table.add_column("Category")

    # Rainfall
    style = Style(color="blue")
    for r in rainfall_ramps:
        table.add_row(r, "Rainfall", style=style)

    table.add_row(*_hline())

    # vegetation
    style = Style(color="green")
    for r in vegetation_ramps:
        table.add_row(r, "Vegetation", style=style)

    table.add_row(*_hline())

    # temperature
    style = Style(color="orange_red1")
    for r in temperature_ramps:
        table.add_row(r, "Temperature", style=style)

    return table


def generate_rainfall_tables(
    ramp_filter: Optional[Tuple[str]] = None,
) -> Iterator[Table]:
    """Generate rainfall ramp tables"""
    yield from _table_gen(".rainfall", rainfall_ramps, ramp_filter)


def generate_vegetation_tables(
    ramp_filter: Optional[Tuple[str]] = None,
) -> Iterator[Table]:
    """Generate vegetation ramp tables"""
    yield from _table_gen(".vegetation", vegetation_ramps, ramp_filter)


def generate_temperature_tables(
    ramp_filter: Optional[Tuple[str]] = None,
) -> Iterator[Table]:
    """Generate temperature ramp tables"""
    yield from _table_gen(".temperature", temperature_ramps, ramp_filter)
