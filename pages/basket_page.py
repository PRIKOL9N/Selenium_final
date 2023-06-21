from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TABLE), \
            "Items is presented, but should not be"

    def should_be_msg_no_item(self):
        print(self.browser.find_element(*BasketPageLocators.NO_ITEM).text)
        assert self.browser.find_element(
            *BasketPageLocators.NO_ITEM).text == 'Your basket is empty. Continue shopping', 'It is not msg, but should be'
