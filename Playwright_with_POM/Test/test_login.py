import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage

def test_login(page: Page):
    login_page = LoginPage(page)

    login_page.open_browser()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    page.wait_for_timeout(5000)