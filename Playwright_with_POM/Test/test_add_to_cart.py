import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.add_to_cart import AddToCart

def test_add_to_cart(page: Page):

    #login -- first
    login_page = LoginPage(page)
    login_page.open_browser()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    page.wait_for_timeout(5000)

    #add to cart
    add_to_cart = AddToCart(page)
    add_to_cart.add_item_to_cart()
    add_to_cart.click_on_cart_icon()
    add_to_cart.click_checkout_icon()
    add_to_cart.enter_first_name("Akash")
    add_to_cart.enter_last_name("Jaiswar")
    add_to_cart.enter_pincode("400022")
    add_to_cart.click_continue_icon()
    add_to_cart.click_finish
    page.wait_for_timeout(5000)