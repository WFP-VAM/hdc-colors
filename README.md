# hdc-colors

This repository contains the color-ramp sources for all* data from the HumanitarianDataCube (HDC), along with some thin python code for user / system interface.

### Installation

```
# mamba/conda
mamba install -c wfp-ram hdc-colors

# pip
pip install --extra-index-url=https://data.earthobservation.vam.wfp.org/pypi/ hdc-colors

```

> **Note**
>
>The main purpose of this repo is to contain the color source, keeping the dependencies minimal. To install all dependencies that might be required for users, please use extras install `hdc-colors[all]`.

### Available color ramps
To see a table with all available color ramps, check out the [rendered markdown](color_ramps.md)!  

Alternatively, the following table can be directly generated using `hdc-colors` by running `hdc-colors-table`.

<div style="width: 100%;">
  <img src="img/hdc-colors-table.svg" style="width: 100%;" alt="hdc-colors ramps">
</div>

To inspect the color ramps for a specific category, you can add the category name to the call (note the lowercase):

```python
hdc-colors-table rainfall
```

and all color ramps for the category will be visualized in the console.

To look at one or more specific ramps, you can add one or more `--filer / -f` flags:

```python
hdc-colors-table rainfall -f rxs
```

<div style="width: 100%;">
  <img src="img/hdc-colors-rxs.svg" style="width: 100%;" alt="hdc-colors rxs-ramp">
</div>

### Usage example

```python
import matplotib.pyplot as plt
import rioxarray

from hdc.colors.rainfall import rxs

# load raster and drop time dim
x = rioxarray.open_rasterio(
    "https://data.earthobservation.vam.wfp.org/docs-data/spi/ethr1s202303d3.tif",
    mask_and_scale=True,
).squeeze()


# need to set min/max and levels but exclude last one (which is inf)
x.plot.imshow(cmap=rxs.cmap, vmin=-2000, vmax=2000, levels=rxs.vals[:-1], extend="both")

# set title
plt.title("Ethiopia SPI-1 ending on the 31st of March, 2023")


```

<div style="width: 100%;">
  <img src="img/ethr1s.svg" style="width: 100%;" alt="Plot example">
</div>
