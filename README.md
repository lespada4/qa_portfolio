# QA Portfolio — Automated Tests with Python + Playwright

This repository contains two automated UI tests using **Python**, **Playwright**, and **pytest**.

## Tests

### 1. GitHub — Open Marzban Repository
- Opens the `gozargah/marzban` repository page
- Verifies that the **"Code"** button is visible

### 2. SauceDemo — Full E2E Purchase Flow
- Logs in as `standard_user`
- Adds a product to the cart
- Proceeds to checkout
- Fills in the order form
- Verifies that the order is successfully completed

## How to Run

```bash
pip install -r requirements.txt
playwright install chromium
pytest test_github.py test_saucedemo.py -v -s
```

**Tech:** Python 3.14, Playwright, pytest.  
**Mode:** `headless=False` (browser visible).

**License:** MIT