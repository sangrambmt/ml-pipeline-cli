# ml-pipeline-cli

Minimal, reproducible data pipeline project built step by step.

Focus:
- environment control
- reproducibility
- pipeline thinking
- data validation contracts

---

## Current Stage

Day 3 — Validation Layer

Pipeline:

CLI → ingest → validate → inspect

---

## Features

### Ingestion
- Read CSV from CLI or `.env`
- Fail-fast on:
  - missing file
  - empty file
  - non-CSV input

### Validation (NEW)
- Schema enforcement (strict column contract)
- Type enforcement using casting (`astype`)
- Null handling (drop rows with nulls)
- Duplicate removal

### Inspection
- Data preview (`head`)
- Schema (`dtypes`)
- Shape

---

## Project Structure

    ml-pipeline-cli/
    │
    ├── src/
    │   ├── main.py              # CLI entry point
    │   ├── ingest.py            # CSV ingestion + inspection
    │   ├── validate.py          # validation + cleaning logic
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

## Expected Input Schema

The pipeline enforces a strict schema:

    id      → int64
    name    → object (string)
    age     → float64
    city    → object (string)

---

## Validation Rules

- Missing columns → pipeline fails
- Incorrect types → auto-cast or fail
- Null values → rows dropped
- Duplicate rows → removed

---

## Example Output

    Reading file: data/raw/sample.csv

    Null values found. Dropping rows with nulls.
    Removed 1 duplicate rows.

    --- Data Preview ---
       id   name   age        city
    0   1  Alice  25.0  Bangalore
    1   2    Bob  30.0     Mumbai

    --- Schema ---
    id        int64
    name     object
    age     float64
    city     object

    --- Shape ---
    (2, 4)

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
- Missing columns → ValueError
- Type conversion failure → TypeError

---

## Dependencies

Defined in `requirements.txt` (version pinned):

- pandas
- python-dotenv

---

## What’s New in Day 3

- Introduced validation layer (`validate.py`)
- Enforced schema contract
- Added null handling
- Added duplicate removal
- Separated ingestion and validation stages

---

## What’s Next

Day 4 — Logging & Observability:

- replace print with logging
- structured logs
- pipeline visibility
- log levels (INFO, ERROR)

---

## End Goal (Week 4)

Full production-style pipeline:

    data → validate → train → model → API → docker

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
- strict data contracts
- modular architecture
- production-oriented practices