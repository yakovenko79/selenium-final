from .base_page import BasePage
from .locators import BasePageLocators
from .locators import ProductPageLocators


class BasketPage(BasePage):
    def is_basket_empty_message(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_MESSAGE), "Basket is not empty"

    def should_not_be_success_message(self):
        # проверяем не присутствует ли название товара и сообщение о добавленном товаре на странице
        assert self.is_not_element_present(*ProductPageLocators.IN_BASKET_BANNER), \
            "Product name is on the page, but shouldn't be"

