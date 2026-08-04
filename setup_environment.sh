#!/usr/bin/env bash
set -euo pipefail

ENV_NAME="xlink-kme-analysis"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd "$REPO_ROOT"
conda env create -f environment.yml
CONDA_BASE="$(conda info --base)"
source "$CONDA_BASE/etc/profile.d/conda.sh"
conda activate "$ENV_NAME"
conda env config vars set -n "$ENV_NAME" LD_LIBRARY_PATH="$CONDA_PREFIX/lib"
python -m ipykernel install --sys-prefix --name "$ENV_NAME" --display-name "Python 3 (xlink-kme-analysis)"

KERNEL_JSON="$CONDA_PREFIX/share/jupyter/kernels/$ENV_NAME/kernel.json"
KERNEL_JSON="$KERNEL_JSON" CONDA_PREFIX="$CONDA_PREFIX" "$CONDA_PREFIX/bin/python" - <<'PY'
import json
import os
from pathlib import Path

kernel_path = Path(os.environ["KERNEL_JSON"])
spec = json.loads(kernel_path.read_text())
spec["env"] = {
    **spec.get("env", {}),
    "LD_LIBRARY_PATH": str(Path(os.environ["CONDA_PREFIX"]) / "lib"),
}
kernel_path.write_text(json.dumps(spec, indent=1) + "\n")
PY

echo "Environment configured: $ENV_NAME"
echo "Select 'Python 3 (xlink-kme-analysis)' as the notebook kernel in VS Code."
