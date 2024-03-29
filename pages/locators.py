from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    REGISTER_PASS1 = (By.CSS_SELECTOR, "input#id_registration-password1")
    REGISTER_PASS2 = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    PRODUCT_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.row h1")
    IN_BASKET_BANNER = (By.CSS_SELECTOR, "div#messages .alert:nth-child(1)")
    IN_BASKET_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong")
    IN_BASKET_TOTAL = (By.CSS_SELECTOR, "div#messages p strong")
    PRODUCT_COST = (By.CSS_SELECTOR, "p.price_color")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group")
    BASKET_CONDITION = (By.CSS_SELECTOR, "div#content_inner")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "div#content_inner > p")
    USER_ICON = (By.CSS_SELECTOR, "i.icon-user")
