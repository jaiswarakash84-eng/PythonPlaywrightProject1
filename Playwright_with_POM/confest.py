# conftest.py
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)  # ✅ 1000ms delay between actions
        page = browser.new_page()
        yield page
        browser.close()