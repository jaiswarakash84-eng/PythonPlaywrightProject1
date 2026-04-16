import pytest
from playwright.sync_api import Page, expect


def test_demo_shop(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    page.click(".ico-register")

    page.click("#gender-male")

    page.fill("#FirstName", "Akash")

    page.fill("#LastName", "Jaiswar")

    page.fill("#Email", "test@gmail.com")

    page.fill("input[name='Password']", "Akash@123")

    page.fill("input[name='ConfirmPassword']", "Akash@123")

    page.click("#register-button")