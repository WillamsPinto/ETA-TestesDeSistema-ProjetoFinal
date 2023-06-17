import time

from selenium.webdriver.common.by import By
from Helpers.session import Session

class ProductComparePage(Session):

    url = 'https://magento.softwaretestingboard.com/catalog/product_compare/'
    class_productName = 'product-item-name'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_compare_page(self):
        return self.driver.current_url == self.url

    def has_product_in_page(self, productName):
        return self.driver.find_element(By.CLASS_NAME, self.class_productName).text.__eq__(productName)