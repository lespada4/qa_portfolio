@echo off
echo Installing dependencies...
pip install -r requirements.txt
python -m playwright install chromium

echo.
echo Running all tests...
python -m pytest test_github.py test_saucedemo.py -v -s

pause