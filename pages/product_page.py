from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket_page(self):
        # нажимаем кнопку "add product"
        basket_link = self.browser.find_element(*ProductPageLocators.PRODUCT_LINK)
        basket_link.click()

    def is_message_after_adding(self):
        # проверяем присутствует ли название товара и сообщение о добавленном товаре на странице
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not on the page"
        assert self.is_element_present(*ProductPageLocators.IN_BASKET_MESSAGE), "Link about adding is not on the page"

        # получаем текст названия товара и текст сообщения о добавлении товара
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        basket_message = self.browser.find_element(*ProductPageLocators.IN_BASKET_MESSAGE).text

        # проверяем, что название товара присутствует в сообщении о добавлении товара
        assert product_name == basket_message, "Product name is not in message"

    def should_be_disappeared(self):
        # проверяем, исчезает ли элемент
        assert self.is_disappeared(*ProductPageLocators.IN_BASKET_BANNER), "Element dont dissapear"

    def should_be_message_about_basket_total(self):
        # проверяем присутствуют ли элементы на странице
        assert self.is_element_present(*ProductPageLocators.PRODUCT_COST), "Price is not on the page"
        assert self.is_element_present(*ProductPageLocators.IN_BASKET_TOTAL), "Price is not in basket"

        # получаем текст цены товара и текст стоимости товаров в корзине
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        basket_total = self.browser.find_element(*ProductPageLocators.IN_BASKET_TOTAL).text

        # сравниваем текст цены товара и текст стоимости товаров в корзине
        assert product_price == basket_total, "Price is not equal"

    def should_not_be_success_message(self):
        # проверяем не присутствует ли название товара и сообщение о добавленном товаре на странице
        assert self.is_not_element_present(*ProductPageLocators.IN_BASKET_BANNER), \
            "Product name is on the page, but shouldn't be"





