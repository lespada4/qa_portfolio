@echo off
echo Installing dependencies...
pip install -r requirements.txt
python -m playwright install chromium

echo Running tests...
python -m pytest test_github.py -v -s

pause