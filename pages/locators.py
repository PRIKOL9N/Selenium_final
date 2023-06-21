from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ITEM_NAME = (By.CSS_SELECTOR, 'div.col-sm-6.product_main h1')
    ITEM_NAME2 = (By.CSS_SELECTOR, 'div.alertinner strong')
    ITEM_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    BASKET_BUTTON = (By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    BASKET_ALERT = (By.CLASS_NAME, 'alertinner')
    BASKET_MSG = (By.CSS_SELECTOR, 'div.alertinner')
    BASKET_VALUE = (By.CSS_SELECTOR, 'div.alertinner p strong')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")


class BasketPageLocators:
    ITEMS_TABLE = (By.CSS_SELECTOR, "div.basket-title.hidden-xs")
    NO_ITEM = (By.CSS_SELECTOR, '#content_inner p')

