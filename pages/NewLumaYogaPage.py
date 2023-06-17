from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

from Helpers.session import Session


class NewLumaYoga(Session):
    url = 'https://magento.softwaretestingboard.com/collections/yoga-new.html'
    first_product = 'product-item-info'
    class_products_list = 'product-item-link'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_newLumaYoga_page(self):
        return self.driver.current_url == self.url

    def get_first_product_name(self):
        product_list = self.driver.find_elements(By.CLASS_NAME, self.class_products_list)
        return product_list[0].text

    def click_first_product_newLumaYoga(self):
        self.driver.find_element(By.CLASS_NAME, self.first_product).click()

