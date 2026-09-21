# Training Tasks

Two standalone Python scripts, no external dependencies, Python 3.8+.

## Structure

```
repo/
  README.md                        ← this file
  task1-classifier/
    classify.py                    ← rule-based message classifier
    messages.txt                   ← 5 input messages
    README.md                      ← task-specific docs
  task2-alert-filter/
    filter_alerts.py               ← critical-event filter
    events.json                    ← 8 events
    README.md                      ← task-specific docs
```

## Quick Start

Run from the **repo root** (or from any directory — scripts resolve paths via `__file__`):

```bash
# Task 1
python task1-classifier/classify.py

# Task 2
python task2-alert-filter/filter_alerts.py
```

No `pip install` needed. Works on Python 3.8+.

## Expected Output

**Task 1** — prints category + draft reply for each of 5 messages.  
**Task 2** — prints 3 critical event names, then `критичных 3`.

See each task's `README.md` for full sample output.
