from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button_basket.click()

    def checking_add_to_basket(self):
        assert self.browser.find_element(
            *ProductPageLocators.BASKET_ALERT).text, 'item was not added to basket'
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        assert item_name == self.browser.find_element(
            *ProductPageLocators.ITEM_NAME2).text, 'The title of the book does not match.'
        assert self.browser.find_elements(*ProductPageLocators.BASKET_MSG)[2], 'No basket value'
        item_price = self.browser.find_element(
            *ProductPageLocators.ITEM_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_VALUE).text
        assert basket_price == item_price, 'Values do not match'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_ALERT), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_after_buy(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_ALERT), \
            "Success message is presented, but should not be"
