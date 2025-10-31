    

# Flask App Testing Process — Summary

## 1. Goal

The goal was to add **unit and functional tests** for a working Flask web application using **pytest**.
Focus: testing app routes, functions, and logic without calling real external APIs or sending emails.

---

## 2. Environment Setup

- Installed all dependencies including `pytest`, `pytest-flask`, and `pytest-cov`.
- Verified the project structure (`application/`, `tests/`, etc.).
- Added `pytest.ini`:

  ```ini
  [pytest]
  testpaths = tests
  pythonpath = .
  ```

```

---

## 3. Test Client Fixture

Created a `conftest.py` file to initialize the Flask app in testing mode:

```python
import pytest
from application.app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
```

This fixture lets tests simulate HTTP requests (`client.get()`, `client.post()`) safely.

---

## 4. Route Tests

Started with basic routes:

* `/` → should return 200 (home page).
* `/login` → should redirect if not logged in.

  Then verified they work using `pytest -v`.

---

## 5. Mocking Data Providers

Used `monkeypatch` to replace real API and email calls:

```python
monkeypatch.setattr("application.jobs_dataframe.fetch_jobs", mock_fetch_jobs)
```

This prevented real network calls and gave predictable test data.

---

## 6. Added Specific Tests

* `/jobs/devops` → renders job table.
* `/jobs/devops/plot` → shows chart and table.
* `/jobs/devops/local-search` → shows local search results.
* `/jobs/filter` → filters job list by location/remote flag.
* `/jobs/devops/notify` → sends mock email (204 response).

---

## 7. Login and Error Tests

Created tests for:

* Successful login with correct credentials.
* Failed login with wrong credentials.
* Invalid route (`/nonexistent`) returns 404.

---

## 8. Function-Level Tests

Directly tested `search_local_jobs()` to ensure local JSON search works correctly.

---

## 9. Coverage

Ran:

```bash
pytest --cov=application --cov-report=term-missing
```

Initial coverage: ~67%

After all tests:  **~72% total coverage** , 100% for key Flask view modules.

---

## 10. Result

* ✅ All 11 tests passed.
* ✅ All routes verified.
* ✅ No external calls made.
* ✅ Simple, maintainable test suite suitable for academic grading.

**Logic Summary:**

1. Start small → verify app runs under test mode.
2. Incrementally add route tests.
3. Mock all external dependencies.
4. Expand coverage to core functions.
5. Verify with coverage report.

---

**Outcome:** A clean, complete pytest-based test suite demonstrating understanding of Flask app testing at a practical homework level.

```

```
