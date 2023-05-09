"""hdc-colors-table script"""
import click
from click.core import Context
from rich.console import Console
from hdc.colors.ui import (
    color_warning,
    create_overview_table,
    generate_rainfall_tables,
    generate_vegetation_tables,
    generate_temperature_tables,
)


def maybe_emit_color_warning(ctx: Context):
    """Emit warning for low colors"""
    if ctx.obj["low_colors"]:
        ctx.obj["console"].print(color_warning())


@click.group(invoke_without_command=True)
@click.option("--help", "cli_help", help="Show help", is_flag=True)
@click.pass_context
def cli(ctx, cli_help):
    """hdc-colors-table entry point"""
    if cli_help:
        click.echo(ctx.get_help())
        ctx.exit()

    click.echo("\n" * 2)
    ctx.ensure_object(dict)
    console = Console()

    if ctx.invoked_subcommand is None:
        table = create_overview_table()
        console.print(table)
        ctx.exit()

    ctx.obj["console"] = console
    ctx.obj["low_colors"] = console.color_system in ("standard", "256")

    maybe_emit_color_warning(ctx)


@cli.command()
@click.pass_context
@click.option("--filter", "-f", "ramp_filter", type=click.STRING, multiple=True)
def rainfall(ctx, ramp_filter):
    """Show rainfall ramps table"""
    console = ctx.obj.get("console")
    for t in generate_rainfall_tables(ramp_filter):
        console.print(t)

    maybe_emit_color_warning(ctx)


@cli.command()
@click.pass_context
@click.option("--filter", "-f", "ramp_filter", type=click.STRING, multiple=True)
def vegetation(ctx, ramp_filter):
    """Show vegetation ramps table"""
    console = ctx.obj.get("console")
    for t in generate_vegetation_tables(ramp_filter):
        console.print(t)

    maybe_emit_color_warning(ctx)


@cli.command()
@click.pass_context
@click.option("--filter", "-f", "ramp_filter", type=click.STRING, multiple=True)
def temperature(ctx, ramp_filter):
    """Show temperature ramps table"""
    console = ctx.obj.get("console")
    for t in generate_temperature_tables(ramp_filter):
        console.print(t)

    maybe_emit_color_warning(ctx)


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
