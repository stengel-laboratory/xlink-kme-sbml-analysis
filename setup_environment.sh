#!/usr/bin/env bash
set -euo pipefail

ENV_NAME="xlink-kme-analysis"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONDA_BASE="$(conda info --base)"

cd "$REPO_ROOT"
if conda env list --json | "$CONDA_BASE/bin/python" -c '
import json
import sys
from pathlib import Path

env_name = sys.argv[1]
environment_names = {Path(path).name for path in json.load(sys.stdin)["envs"]}
sys.exit(env_name not in environment_names)
' "$ENV_NAME"; then
    conda env update -n "$ENV_NAME" -f environment.yml --prune
else
    conda env create -n "$ENV_NAME" -f environment.yml
fi
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
