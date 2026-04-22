# ml-pipeline-cli

Minimal, reproducible data pipeline project built step by step.

Focus:
- environment control
- reproducibility
- pipeline thinking

---

## Current Stage

Day 2 — CSV Ingestion

Pipeline:

CLI → load_csv → inspect

---

## Features

- CLI-based execution using argparse
- Config-driven paths using `.env`
- CSV ingestion using pandas
- Fail-fast error handling:
  - missing file
  - empty file
  - non-CSV input
- Data inspection:
  - preview (head)
  - schema (dtypes)
  - shape

---

## Project Structure

    ml-pipeline-cli/
    │
    ├── src/
    │   ├── main.py              # entry point (CLI)
    │   ├── ingest.py            # CSV ingestion + inspection
    │   └── utils/               # (reserved)
    │
    ├── data/
    │   ├── raw/                 # input CSV files
    │   └── processed/           # cleaned data (future)
    │
    ├── output/                  # pipeline outputs (future)
    ├── logs/                    # logs (future)
    │
    ├── .env                     # environment config
    ├── .gitignore
    ├── requirements.txt
    └── README.md

---

## Setup

Create virtual environment:

    python -m venv venv

Activate:

Windows:

    venv\Scripts\activate

Mac/Linux:

    source venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

---

## Run

Using CLI:

    python src/main.py --input data/raw/sample.csv

Using `.env` fallback:

    INPUT_DIR=data/raw

Then run:

    python src/main.py

---

## Example Output

    Reading file: data/raw/sample.csv

    --- Data Preview ---
       id     name   age  salary
    0   1    Alice  25.0   50000
    1   2      Bob  30.0   60000
    2   3  Charlie   NaN   70000

    --- Schema ---
    id          int64
    name       object
    age       float64
    salary      int64

    --- Shape ---
    (4, 4)

---

## Environment Config (.env)

    APP_ENV=dev
    LOG_LEVEL=INFO
    INPUT_DIR=data/raw
    OUTPUT_DIR=data/processed

---

## Error Handling

The pipeline fails fast:

- File not found → FileNotFoundError
- Empty CSV → ValueError
- Non-CSV input → ValueError

---

## Dependencies

Defined in `requirements.txt` (version pinned):

- pandas
- python-dotenv

---

## What’s Next

Day 3 — Validation Layer:

- null handling
- duplicate removal
- schema validation
- data cleaning

---

## End Goal (Week 4)

Full pipeline:

    data → validation → training → model → API → docker

Single repo containing:

- CLI pipeline
- versioned data (DVC)
- containerized execution (Docker)
- model training
- FastAPI serving

---

## Purpose

This project simulates real MLOps workflows:

- reproducible pipelines
- modular architecture
- production-oriented practices