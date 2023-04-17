from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")


class ProductPageLocators():
    PRODUCT_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.row h1")
    IN_BASKET_BANNER = (By.CSS_SELECTOR, "div#messages .alert:nth-child(1)")
    IN_BASKET_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong")
    IN_BASKET_TOTAL = (By.CSS_SELECTOR, "div#messages p strong")
    PRODUCT_COST = (By.CSS_SELECTOR, "p.price_color")

