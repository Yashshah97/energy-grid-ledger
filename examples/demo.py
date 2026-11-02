"""Demo for Energy Grid Append-Only Ledger."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import energy_grid_ledger

print("Energy Grid Append-Only Ledger", "v" + energy_grid_ledger.__version__)
print("modules:", [m for m in dir(energy_grid_ledger) if not m.startswith('_')])
