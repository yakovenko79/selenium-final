import time
import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage

link_promo = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
link_product = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
link_login = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = LoginPage(browser, link_login)
        self.page.open()
        self.page.register_new_user(email=str(time.time()) + "@fakemail.org", password="q1w23r4t5y6")
        self.page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link_product)
        page.open()
        page.add_to_basket_page()
        page.is_message_after_adding()
        page.should_be_message_about_basket_total()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link_product)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link_promo)
    page.open()
    page.add_to_basket_page()
    page.solve_quiz_and_get_code()
    page.is_message_after_adding()
    page.should_be_message_about_basket_total()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, url=browser.current_url)
    basket_page.should_not_be_success_message()
    basket_page.is_basket_empty_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link_promo)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_promo)
    page.open()
    page.add_to_basket_page()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_promo)
    page.open()
    page.add_to_basket_page()
    page.solve_quiz_and_get_code()
    page.is_message_after_adding()
    page.should_be_disappeared()
