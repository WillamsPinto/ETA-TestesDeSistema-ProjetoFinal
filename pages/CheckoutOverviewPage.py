from selenium.webdriver.common.by import By

from Helpers.session import Session


class CheckoutOverviewPage(Session):
    url = 'https://www.saucedemo.com/checkout-step-two.html'
    txt_checkout_overview_title = 'Checkout: Overview'
    id_finish_btn = 'finish'
    class_product_item = 'inventory_item_name'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_checkout_overview_page(self):
        return self.is_page(url=self.url, title=self.txt_checkout_overview_title)

    def click_finish(self):
        self.driver.find_element(By.ID, self.id_finish_btn).click()

    def has_product_in_list(self, product_name):
        product_list = self.driver.find_elements(By.CLASS_NAME, self.class_product_item)

        for product in product_list:
            if product.text == product_name:
                return True
        return False