import pytest
from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self,page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")

    #Actions

    def open_browser(self):
        self.page.goto("https://www.saucedemo.com/")

    def enter_username(self,username):
        self.username.fill(username)

    def enter_password(self, password):
        self.password.fill(password)

    def click_login(self):
        self.login_button.click()

