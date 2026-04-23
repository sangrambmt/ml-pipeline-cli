# ml-pipeline-cli

Minimal, reproducible data pipeline built with MLOps practices.

---

## Overview

This project implements a structured data pipeline with:

- CLI-based execution
- Data validation and cleaning
- Structured logging
- Data versioning using DVC
- Reproducible pipeline execution

---

## Pipeline Flow

raw.csv → ingest → validate → clean.csv

Execution:

CLI → ingest → validate → save → DVC pipeline

---

## Features

### Ingestion
- CSV loading via CLI or .env
- Fail-fast on missing or invalid files

### Validation
- Schema enforcement
- Type casting (astype)
- Null handling (row removal)
- Duplicate removal

### Logging
- Structured logs (INFO, WARNING, ERROR)
- Console + file output (logs/pipeline.log)

### Data Versioning (DVC)
- Raw data tracked via DVC
- Git tracks metadata only
- Supports reproducibility

### Pipeline (DVC)
- Defined in dvc.yaml
- Runs only when inputs change
- Tracks dependencies and outputs

---

## Project Structure

    ml-pipeline-cli/
    │
    ├── src/
    │   ├── main.py
    │   ├── ingest.py
    │   ├── validate.py
    │   ├── logger.py
    │
    ├── data/
    │   ├── raw/
    │   └── processed/
    │
    ├── logs/
    │
    ├── dvc.yaml
    ├── dvc.lock
    ├── .dvc/
    ├── .env
    ├── requirements.txt
    └── README.md

---

## Setup

Create environment:

    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt

---

## Run

Direct execution:

    python src/main.py --input data/raw/sample.csv

DVC pipeline execution:

    dvc repro

---

## DVC Workflow

Track dataset:

    git rm --cached data/raw/sample.csv
    dvc add data/raw/sample.csv
    git add .gitignore data/raw/sample.csv.dvc
    git commit -m "track dataset with dvc"

Create pipeline:

    dvc stage add -n preprocess -d src/main.py -d src/ingest.py -d src/validate.py -d data/raw/sample.csv -o data/processed/clean.csv python src/main.py --input data/raw/sample.csv

Run pipeline:

    dvc repro

---

## Pipeline Behavior

- No change → skips execution  
- Data changed → re-runs pipeline  
- Code changed → re-runs pipeline  

---

## Example Output

    Loaded data shape: (83, 4)
    Null cells found: 20
    Rows containing nulls: 18
    Shape after null removal: (65, 4)
    Duplicates removed: 1
    Final shape: (64, 4)

---

## Environment Configuration

    APP_ENV=dev
    LOG_LEVEL=INFO
    INPUT_DIR=data/raw
    OUTPUT_DIR=data/processed

---

## Key Concepts

- Git → tracks code  
- DVC → tracks data  
- dvc.yaml → defines pipeline  
- dvc.lock → locks pipeline state  

---

## What’s Implemented

- CLI pipeline execution  
- Data validation layer  
- Logging system  
- Data versioning (DVC)  
- Reproducible pipeline  

---

## End Goal

data → validate → train → model → API → docker

---

## Purpose

This project simulates real-world MLOps systems:

- reproducible pipelines  
- data + code versioning  
- modular architecture  
- production-oriented workflow  