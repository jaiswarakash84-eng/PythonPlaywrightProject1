import pytest
from playwright.sync_api import Page, expect

class AddToCart:
    def __init__(self, page):
        self.page = page
        self.add_to_cart = page.locator("#add-to-cart-sauce-labs-backpack")
        self.click_on_cart = page.locator(".shopping_cart_badge")
        self.checkout_button = page.locator("button[data-test='checkout']")
        self.enter_first_name_input = page.locator("#first-name")
        self.enter_last_name_input = page.locator("#last-name")
        self.enter_pincode_input = page.locator("#postal-code")
        self.click_continue = page.locator("input[data-test='continue']")
        self.click_finish = page.locator("input[data-test='finish']")

    #Actions

    def add_item_to_cart(self):
        self.add_to_cart.click()

    def click_on_cart_icon(self):
        self.click_on_cart.click()

    def click_checkout_icon(self):
        self.checkout_button.click()

    def enter_first_name(self,first_name):
        self.enter_first_name_input.fill(first_name)

    def enter_last_name(self,last_name):
        self.enter_last_name_input.fill(last_name)

    def enter_pincode(self,pincode):
        self.enter_pincode_input.fill(pincode)

    def click_continue_icon(self):
        self.click_continue.click()

    def click_finish_icon(self):
        self.click_finish.click()