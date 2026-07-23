# QA Portfolio — GitHub Search Test

Automated test for GitHub search using Python + Playwright.

**Scenario:**  
Open GitHub → search "pytest" → open `pytest-dev/pytest` repo → verify "Code" button is visible.

**Run:**
```bash
pip install -r requirements.txt
playwright install chromium
pytest tests/test_github.py -v -s
```

**Tech:** Python 3.14, Playwright, pytest.  
**Mode:** `headless=False` (browser visible).

**License:** MIT