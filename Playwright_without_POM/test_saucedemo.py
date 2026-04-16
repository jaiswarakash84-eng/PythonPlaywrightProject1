import pytest
from playwright.sync_api import Page,expect

def test_login(page:Page):
    page.goto("https://www.saucedemo.com/")

    page.fill("input[data-test='username']","standard_user")

    page.fill("input[data-test='password']", "secret_sauce")

    page.click("input[data-test='login-button']")

    page.wait_for_timeout(5000)

    page.click("button[data-test='add-to-cart-sauce-labs-bolt-t-shirt']")

    page.click(".shopping_cart_badge")

    page.click("#checkout")

    page.fill("#first-name", "Akash")

    page.fill("#last-name", "jaiswar")

    page.fill("#postal-code", "400022")

    page.click("#continue")

    page.click("#finish")

    page.click("#back-to-products")

    page.click("#react-burger-menu-btn")

    page.click("#logout_sidebar_link")