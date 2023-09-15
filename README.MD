# XLINK KME SBML Analysis
## Analysis & Visualization of xl-kme models
### 2023-09 Kai-Michael Kammer
Analysis & Visualization of Models created by the Kinetic Simulation Framework for Crosslinks (https://github.com/stengel-laboratory/xlink-kme-sbml).

## Installation
This package requires Tellurium installed. Also required is the prot_tools package from https://github.com/stengel-laboratory/prot-tools  
Requires the Kinetic Simulation Framework for Crosslinks (https://github.com/stengel-laboratory/xlink-kme-sbml) to be installed.  
Uses altair for visualization: https://github.com/altair-viz/altair  
Also required are a number of libraries used by altair: vegafusion, vegafusion-python-embed and vl-convert-python. All required packages are listed in the setup.py

## Usage
There are two Jupyter notebooks. 

1) paper_sim_only: runs the kinetic simulations via Tellurium. The required protein models are inside the protein_models folder and were previouly created using the Kinetic Simulation Framework for Crosslinks.
2) paper_viz_only: plots various visualizations from the simulation output created by paper_sim_only. This output is already included inside the Github repository.
