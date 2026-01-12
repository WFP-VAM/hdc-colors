"""hdc-colors-create-ctable script."""

import click

import hdc.colors.hazards as hazards_ramps
import hdc.colors.rainfall as rainfall_ramps
import hdc.colors.temperature as temperature_ramps
import hdc.colors.vegetation as vegetation_ramps

ALL_RAMPS = [rainfall_ramps, vegetation_ramps, temperature_ramps, hazards_ramps]


def get_ramp(ramp_name: str):
    """Get ramp."""
    for ramp in ALL_RAMPS:
        for rr in ramp.__all__:
            if rr == ramp_name:
                return getattr(ramp, ramp_name)
    return None


@click.command()
@click.argument("ramp-name", type=click.STRING)
@click.option("--write", is_flag=True, help="write to disk")
@click.option("-f", "--file-name", type=str, help="output filename")
@click.option("-n", "--nodata", type=(int, float), help="nodata value")
def cli(ramp_name, write, file_name, nodata):
    """hdc-colors-create-ctable entry point."""
    ramp_name = ramp_name.lower()
    cramp = get_ramp(ramp_name)

    if write:
        file_name = file_name if file_name else ramp_name

    print(cramp.to_txt(file_name, nodata))


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
