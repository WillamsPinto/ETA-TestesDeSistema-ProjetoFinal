import time

from selenium.webdriver.common.by import By
from Helpers.session import Session

class ShoppingCartPage(Session):

    url = 'https://magento.softwaretestingboard.com/checkout/cart/'
    text_ShoppingCartPage_title = 'Shopping Cart'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_ShoppingCartPage_page(self):
        return self.is_page(self.url, self.text_ShoppingCartPage_title)