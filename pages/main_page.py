from .base_page import BasePage
from .locators import MainPageLocators
from.login_page import LoginPage
from .locators import ProductPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        alert = self.browser.switch_to.alert
        alert.accept()
        #return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

'''    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*ProductPageLocators.PRODUCT_LINK)
        basket_link.click()'''