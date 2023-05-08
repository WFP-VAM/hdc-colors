"""hdc-colors-table script"""
import click
from rich.console import Console
from hdc.colors.ui import (
    create_overview_table,
    generate_rainfall_tables,
    generate_vegetation_tables,
    generate_temperature_tables,
)


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


@cli.command()
@click.pass_context
@click.option("--filter", "ramp_filter", type=click.STRING, multiple=True)
def rainfall(ctx, ramp_filter):
    """Show rainfall ramps table"""
    console = ctx.obj.get("console")
    for t in generate_rainfall_tables(ramp_filter):
        console.print(t)


@cli.command()
@click.pass_context
@click.option("--filter", "ramp_filter", type=click.STRING, multiple=True)
def vegetation(ctx, ramp_filter):
    """Show vegetation ramps table"""
    console = ctx.obj.get("console")
    for t in generate_vegetation_tables(ramp_filter):
        console.print(t)


@cli.command()
@click.pass_context
@click.option("--filter", "ramp_filter", type=click.STRING, multiple=True)
def temperature(ctx, ramp_filter):
    """Show temperature ramps table"""
    console = ctx.obj.get("console")
    for t in generate_temperature_tables(ramp_filter):
        console.print(t)


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
