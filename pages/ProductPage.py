import time

from selenium.webdriver.common.by import By
from Helpers.session import Session

class ProductPage(Session):

    first_product_hoodies = 'product-item-info'
    id_product_sizes = 'option-label-size-143-item-166'
    id_product_colors = 'option-label-color-93-item-52'
    add_product_button = 'product-addtocart-button'
    xpath_success_message_product_to_cart = '//*[@id="maincontent"]/div[1]/div[2]/div/div/div'
    success_message_product_to_cart = 'You added Circe Hooded Ice Fleece to your shopping cart.'
    xpath_value_cart = '/html/body/div[1]/header/div[2]/div[1]/a/span[2]/span[1]'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_product_page(self, nome_primeiro_produto_hoodies):
        product_url = 'https://magento.softwaretestingboard.com/'+nome_primeiro_produto_hoodies.replace(' ', '-')+'.html'
        return self.is_page(product_url.lower(), nome_primeiro_produto_hoodies)

    def click_first_product_hoddies(self):
        self.driver.find_element(By.CLASS_NAME, self.first_product_hoodies).click()

    def add_product_in_cart(self):
        self.driver.find_element(By.ID, self.id_product_sizes).click()
        self.driver.find_element(By.ID, self.id_product_colors).click()
        self.driver.find_element(By.ID, self.add_product_button).click()

    def has_success_message_product_to_cart(self):
        time.sleep(2.5)
        message = self.driver.find_element(By.XPATH, self.xpath_success_message_product_to_cart).text
        return self.success_message_product_to_cart.__eq__(message)

    def has_product_added_to_cart(self, count):
        return self.driver.find_element(By.XPATH, self.xpath_value_cart).text.__eq__(count)