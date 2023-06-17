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
    xpath_compare_opt = '//*[@id="maincontent"]/div[2]/div/div[1]/div[5]/div/a[2]'
    success_message_add_compare_list = "You added product Echo Fit Compression Short to the comparison list."
    xpath_compare_list_link = '//*[@id="maincontent"]/div[1]/div[2]/div/div/div/a'
    id_xs_size_opt = 'option-label-size-143-item-166'
    id_blue_color_opt = 'option-label-color-93-item-50'
    attribute_aria_checked = 'aria-checked'
    id_quant_field = 'qty'
    xpath_cart_icon = '/html/body/div[1]/header/div[2]/div[1]/a'
    xpath_viewCart_link = '//*[@id="minicart-content-wrapper"]/div[2]/div[5]/div/a/span'
    xpath_trash_of_cart = '//*[@id="mini-cart"]/li/div/div/div[3]/div[2]/a'
    text_empty_cart = 'You have no items in your shopping cart.'
    xpath_empty_cart_message = '//*[@id="minicart-content-wrapper"]/div[2]/strong'

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

    def click_in_add_button(self):
        self.driver.find_element(By.ID, self.add_product_button).click()

    def has_success_message_product_to_cart(self):
        time.sleep(2.5)
        message = self.driver.find_element(By.XPATH, self.xpath_success_message_product_to_cart).text
        return self.success_message_product_to_cart.__eq__(message)

    def has_product_added_to_cart(self, count):
        return self.driver.find_element(By.XPATH, self.xpath_value_cart).text.__eq__(count)

    def click_in_compare_option(self):
        self.driver.find_element(By.XPATH, self.xpath_compare_opt).click()

    def has_add_product_in_compare_list_successfully(self):
        time.sleep(2.5)
        return self.driver.find_element(By.XPATH, self.xpath_success_message_product_to_cart).text.__eq__(self.success_message_add_compare_list)

    def click_in_compare_list_link(self):
        self.driver.find_element(By.XPATH, self.xpath_compare_list_link).click()

    def click_in_xs_size(self):
        self.driver.find_element(By.ID, self.id_xs_size_opt).click()

    def xs_size_was_selected(self):
        return self.driver.find_element(By.ID, self.id_xs_size_opt).get_attribute(self.attribute_aria_checked)

    def click_in_blue_color(self):
        self.driver.find_element(By.ID, self.id_blue_color_opt).click()

    def blue_color_was_selected(self):
        return self.driver.find_element(By.ID, self.id_blue_color_opt).get_attribute(self.attribute_aria_checked)

    def insert_quant_value(self, quant):
        self.driver.find_element(By.ID, self.id_quant_field).clear()
        self.driver.find_element(By.ID, self.id_quant_field).send_keys(quant)

    def click_in_cart_icon(self):
        time.sleep(3.5)
        self.driver.find_element(By.XPATH, self.xpath_cart_icon).click()

    def click_in_view_cart_link(self):
        self.driver.find_element(By.XPATH, self.xpath_viewCart_link).click()

    def click_in_cart_trash_icon(self):
        self.driver.find_element(By.XPATH, self.xpath_trash_of_cart).click()

    def click_in_ok_button(self):
        self.driver.find_element(By.XPATH, "/html/body/div[3]/aside[2]/div[2]/footer/button[2]").click()

    def has_cart_empty_message(self):
        time.sleep(2.5)
        return self.driver.find_element(By.XPATH, self.xpath_empty_cart_message).text.__eq__(self.text_empty_cart)