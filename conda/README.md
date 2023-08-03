Conda packaging for hdc-colors
==============================

To install in conda

```bash
conda activate myenv
conda install -c wfp-ram hdc-colors
```

Or when defining environment

```yaml
name: myenv
channels:
  - conda-forge
  - wfp-ram
dependencies:
  - python=3.10
  - hdc-colors
```

Or add it to channel list

```bash
conda config --append channels wfp-ram 
```
