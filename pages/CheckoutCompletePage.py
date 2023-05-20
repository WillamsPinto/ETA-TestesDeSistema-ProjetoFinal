from selenium.webdriver.common.by import By

from Helpers.session import Session


class CheckoutCompletePage(Session):

    url = 'https://www.saucedemo.com/checkout-complete.html'
    txt_checkout_title = 'Checkout: Complete!'
    txt_thank_order = 'Thank you for your order!'
    class_thank_order = 'complete-header'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_checkout_complete_page(self):
        return self.is_page(url=self.url, title=self.txt_checkout_title)

    def has_thank_order_text(self):
        return self.driver.find_element(By.CLASS_NAME, self.class_thank_order).text == self.txt_thank_order