import pytest
from playwright.sync_api import Page, expect

class LogoutPage:
    def __init__(self, page):
        self.page = page
        self.hamburger_menu = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")

    def click_menu(self):
        self.hamburger_menu.click()

    def click_logout(self):
        self.logout_link.click()

