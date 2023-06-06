Conda packaging for hdc-colors 
==============================

To install in conda

```bash
conda activate myenv
conda install -c https://data.earthobservation.vam.wfp.org/hdc hdc-colors
```

Or when defining environment

```yaml
name: myenv
channels:
  - https://conda.anaconda.org/conda-forge
  - https://data.earthobservation.vam.wfp.org/hdc
dependencies:
  - python=3.10
  - hdc-colors
```

Or add it to channel list

```bash
conda config --append channels https://data.earthobservation.vam.wfp.org/hdc
```
