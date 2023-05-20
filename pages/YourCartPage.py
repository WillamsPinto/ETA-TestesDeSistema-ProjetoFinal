from selenium.webdriver.common.by import By

from Helpers.session import Session


class YourCartPage(Session):

    url = 'https://www.saucedemo.com/cart.html'
    txt_your_cart_title = 'Your Cart'
    id_checkout_btn = 'checkout'
    class_product_item = 'inventory_item_name'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_your_cart_page(self):
        return self.is_page(self.url, self.txt_your_cart_title)

    def click_checkout(self):
        self.driver.find_element(By.ID, self.id_checkout_btn).click()

    def has_product_in_cart(self, product_name):
        product_list = self.driver.find_elements(By.CLASS_NAME, self.class_product_item)
        print(f'Numero de produtos na lista: {len(product_list)}')

        for product in product_list:
            if product.text == product_name:
                return True
        return False



