## Commands Used (Pipeline Setup)

| Step               | Command                                          | Purpose                    |
| ------------------ | ------------------------------------------------ | -------------------------- |
| Project Setup      | `mkdir ml-pipeline-cli`                          | Create project folder      |
| Navigate           | `cd ml-pipeline-cli`                             | Move into project          |
| Create venv        | `python -m venv venv`                            | Create virtual environment |
| Activate (Windows) | `venv\Scripts\activate`                          | Start virtual environment  |
| Install packages   | `pip install pandas python-dotenv dvc`           | Install dependencies       |
| Freeze deps        | `pip freeze > requirements.txt`                  | Save exact versions        |
| Create folders     | `mkdir src data output logs`                     | Project structure          |
| Create subfolders  | `mkdir data\raw data\processed`                  | Data directories           |
| Run script         | `python src/main.py`                             | Execute pipeline           |
| Run with input     | `python src/main.py --input data/raw/sample.csv` | CLI execution              |

---

## Git Commands

| Step               | Command                       | Purpose               |
| ------------------ | ----------------------------- | --------------------- |
| Init repo          | `git init`                    | Start version control |
| Check status       | `git status`                  | See changes           |
| Stage files        | `git add .`                   | Add all changes       |
| Commit             | `git commit -m "message"`     | Save version          |
| Add remote         | `git remote add origin <url>` | Connect to GitHub     |
| Check remote       | `git remote -v`               | Verify remote         |
| First push         | `git branch -M main`          | Set branch name       |
| Push               | `git push -u origin main`     | Push to GitHub        |
| Regular push       | `git push`                    | Push updates          |
| View history       | `git log --oneline`           | See commits           |
| Diff (unstaged)    | `git diff`                    | See changes           |
| Diff (last commit) | `git diff HEAD~1`             | Compare versions      |
| Diff specific      | `git diff src/main.py`        | File-level diff       |

---

## Git Pager / Diff Control

| Command | Purpose            |
| ------- | ------------------ |
| `q`     | Exit diff view     |
| `/text` | Search inside diff |
| `space` | Scroll             |

---

## Advanced Git (Used / Mentioned)

| Command                         | Purpose             |
| ------------------------------- | ------------------- |
| `git diff --name-only`          | Show changed files  |
| `git diff --staged`             | Show staged changes |
| `git pull origin main --rebase` | Fix push conflicts  |

---

## Environment Management

| Command      | Purpose                  |
| ------------ | ------------------------ |
| `deactivate` | Exit virtual environment |

---

## Debug / Cleanup

| Command                 | Purpose                        |
| ----------------------- | ------------------------------ |
| `rm -r src/__pycache__` | Remove cache (Linux/Mac)       |
| Delete manually         | Remove `__pycache__` (Windows) |

---

## Run Variations

| Command                               | Purpose               |
| ------------------------------------- | --------------------- |
| `python src/main.py`                  | Run using `.env`      |
| `python src/main.py --input file.csv` | Run with custom input |

---

# 🆕 DVC Commands (Day 6)

## DVC Setup

| Command                  | Purpose                |
| ------------------------ | ---------------------- |
| `pip install dvc`        | Install DVC            |
| `dvc init`               | Initialize DVC         |
| `git add .dvc .dvcignore`| Track DVC config       |
| `git commit -m "chore: initialize dvc"` | Commit setup |

---

## DVC Data Tracking

| Command                                      | Purpose                          |
| -------------------------------------------- | -------------------------------- |
| `git rm --cached data/raw/sample.csv`        | Remove file from Git tracking     |
| `dvc add data/raw/sample.csv`                | Track file with DVC              |
| `git add .gitignore data/raw/sample.csv.dvc` | Add DVC metadata                 |
| `git commit -m "data: track dataset with dvc"` | Commit data tracking           |

---

## DVC Pipeline

| Command | Purpose |
|--------|--------|
| `dvc stage add -n preprocess -d src/main.py -d src/ingest.py -d src/validate.py -d data/raw/sample.csv -o data/processed/clean.csv python src/main.py --input data/raw/sample.csv` | Create pipeline stage |
| `dvc repro` | Run pipeline |
| `dvc dag` | View pipeline graph |

---

## DVC Versioning & Execution

| Command | Purpose |
|--------|--------|
| `dvc repro` | Re-run only if changes detected |
| `dvc checkout` | Restore data from cache |
| `dvc push` | Push data to remote storage |

---

## DVC Config

| Command | Purpose |
|--------|--------|
| `dvc config core.autostage true` | Auto stage dvc.lock changes |

---