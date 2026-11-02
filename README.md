# Energy Grid Append-Only Ledger

This is an append-only ledger designed to securely record power load forecasts, ensuring the integrity of energy grid data through tamper-evident hashing and chaining of events. Built from scratch in Python for maximum flexibility and maintainability, this project includes comprehensive testing and documentation. By leveraging these features, users can trust their data and make informed decisions about energy management.

## What makes it unique

Combines power load forecasting with a tamper-evident hash-chained event log — a niche where few ready-made tools exist.

## Features

- **`energy_grid_ledger/ledgers.py`** — Implementation of the append-only ledger
- **`energy_grid_ledger/events.py`** — Representation of individual events within the ledger
- **`energy_grid_ledger/hash_chains.py`** — Hash-chained log implementation
- **`energy_grid_ledger/tests_test_ledgers.py`** — Unit tests for the ledger functionality
- **`energy_grid_ledger/utils_hashing.py`** — Utility functions for hashing and cryptographic operations
- **`energy_grid_ledger/core.py`** — main domain logic and public entry points

## Tech stack

- **Python 3** — pure standard library, **zero external dependencies**
- **unittest** for the test suite (6/6 module suites passing)
- Local-first: no network calls, no API keys, runs anywhere Python runs

## How to run

```bash
git clone https://github.com/Yashshah97/energy-grid-ledger.git
cd energy-grid-ledger

# run the demo
python3 examples/demo.py

# run the tests
python3 -m unittest discover -s tests -t .
```

No installation step is needed — there is nothing to `pip install`.

## Project structure

```
energy-grid-ledger/
├── energy_grid_ledger/
│   ├── ledgers.py
│   ├── events.py
│   ├── hash_chains.py
│   ├── tests_test_ledgers.py
│   ├── utils_hashing.py
│   ├── core.py
├── tests/               # unittest suite (verified passing)
├── examples/demo.py     # runnable demo (verified)
├── docs/
└── README.md
```

See [docs/PLAN.md](docs/PLAN.md) for the architecture and
[docs/usage.md](docs/usage.md) for API notes.

## About

Domain: **energy-grid** · Archetype: **ledger** ·
Built autonomously by JARVIS on 2026-11-02. MIT licensed.
