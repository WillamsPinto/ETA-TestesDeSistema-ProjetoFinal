from selenium.webdriver.common.by import By

from Helpers.session import Session


class CheckoutInformationPage(Session):

    url = 'https://www.saucedemo.com/checkout-step-one.html'
    txt_checkout_title = 'Checkout: Your Information'
    id_continue_btn = 'continue'
    txt_error_first_name_msg = 'Error: First Name is required'
    class_error_first_name = 'error-message-container'
    id_first_name = 'first-name'
    id_last_name = 'last-name'
    id_postal_code = 'postal-code'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_checkout_information_page(self):
        return self.is_page(self.url, self.txt_checkout_title)

    def click_continue(self):
        self.driver.find_element(By.ID, self.id_continue_btn).click()

    def has_first_name_error(self):
        return self.driver.find_element(By.CLASS_NAME, self.class_error_first_name).text == self.txt_error_first_name_msg

    def fill_information_checkout(self, name, last, postal_code):
        self.fill_first_name(name)
        self.driver.find_element(By.ID, self.id_last_name).send_keys(last)
        self.driver.find_element(By.ID, self.id_postal_code).send_keys(postal_code)
        self.click_continue()

    def fill_first_name(self, name):
        self.driver.find_element(By.ID, self.id_first_name).send_keys(name)