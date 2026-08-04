# XLINK KME SBML Analysis

## Analysis & Visualization of xl-kme models

### 2023-09 Kai-Michael Kammer

Analysis & Visualization of Models created by the Kinetic Simulation Framework for Crosslinks (<https://github.com/stengel-laboratory/xlink-kme-sbml>).

## Installation

This package requires Tellurium installed. Also required is the prot_tools package from <https://github.com/stengel-laboratory/prot-tools>
Requires the Kinetic Simulation Framework for Crosslinks (<https://github.com/stengel-laboratory/xlink-kme-sbml>) to be installed.
Uses altair for visualization: <https://github.com/altair-viz/altair>
Also required are a number of libraries used by altair installable with altair-all (conda) or altair[all] (pip). All required packages are listed in the setup.py.

### Conda environment

The notebooks use Python 3.10 because the Tellurium/RoadRunner native wheels
are not compatible with every newer Python version. From this repository, run
the one-time setup script:

```bash
bash setup_environment.sh
```

The script creates the environment from `environment.yml`, installs the current
default branch of `xlink-kme-sbml` from its public Git repository, stores the
native library path in the conda environment, and registers a Jupyter kernel
containing that path. The three xlink-kme repositories are maintained in sync,
so this workflow follows the corresponding upstream model-library changes. VS
Code does not need to be started from a terminal and no manual
`LD_LIBRARY_PATH` export is needed later. Select `Python 3
(xlink-kme-analysis)` as the notebook kernel.

The checked-in protein models contain all four XML variants required by
`paper_sim_only.ipynb`. Generating new protein models requires the corresponding
fix in the upstream `xlink-kme-sbml` repository, not this analysis repository.

## Usage

There are two Jupyter notebooks.

1) paper_sim_only: runs the kinetic simulations via Tellurium. The required protein models are inside the protein_models folder and were previouly created using the Kinetic Simulation Framework for Crosslinks.
2) paper_viz_only: plots various visualizations from the simulation output created by paper_sim_only. This output is already included inside the Github repository.
