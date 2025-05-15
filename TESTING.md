# Testing Guide

This document outlines both a **manual test plan** template and **automated test instructions** for the Autonomous Research Agent.

---

## 1. Manual Test Plan Template

Use this table to record manual test results as you interact with the system:

| Test Case ID | Module      | Input                           | Expected Output                              | Actual Output | Pass/Fail | Notes |
| ------------ | ----------- | ------------------------------- | -------------------------------------------- | ------------- | --------- | ----- |
| TC-001       | planner.py  | “How will AI impact transport?” | List of 3–7 actionable subtasks              |               |           |       |
| TC-002       | executor.py | \[list of subtasks]             | Dict mapping each task to a text result      |               |           |       |
| TC-003       | memory.py   | Results dict                    | Appends entry to `data/memory.json`          |               |           |       |
| TC-004       | reporter.py | Results dict                    | MD file in `reports/` with formatted content |               |           |       |

---

## 2. Automated Test Instructions (pytest)

We use **pytest** for unit testing. The `tests/` directory contains stub files for each module:

```bash
# Install test dependencies
pip install pytest

# Run all tests
pytest
```

### Test Structure

* `tests/test_planner.py` — verifies `generate_plan` returns a list and stubbed subtasks.
* `tests/test_executor.py` — verifies `execute_tasks` returns a dict mapping tasks to results.
* `tests/test_memory.py` — checks saving and loading memory JSON.
* `tests/test_reporter.py` — ensures filename sanitization and report file creation.

### Adding New Tests

1. Create a new file `tests/test_<module>.py`.
2. Import target function and write assertions.
3. Use fixtures or `monkeypatch` to stub external dependencies.

---

By following this guide, your testing will be both repeatable and maintainable, ensuring high confidence as the project evolves.
