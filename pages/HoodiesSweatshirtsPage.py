import time

from selenium.webdriver.common.by import By
from Helpers.session import Session

class HoodiesSweatshirtsPage(Session):

    first_produc_hoodies = 'product-item-info'
    url = 'https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html'
    url_by_price = 'https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html?product_list_order=price'
    text_HoodiesSweatshirts_title = "Hoodies & Sweatshirts"
    class_products_list = 'product-item-link'
    id_modeList = 'mode-list'
    id_sorter_list = 'sorter'
    xpath_view_mode_list = '//*[@id="maincontent"]/div[3]/div[1]/div[3]'
    xpath_order_by_price = '//*[@id="sorter"]/option[3]'
    class_view_mode_list = 'products wrapper list products-list'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_HoodiesSweatshirts_page(self):
        return self.is_page(self.url, self.text_HoodiesSweatshirts_title)

    def get_product_name(self):
        lista_produtos = self.driver.find_elements(By.CLASS_NAME, self.class_products_list)
        return lista_produtos[0].text

    def click_first_product_hoddies(self):
        self.driver.find_element(By.CLASS_NAME, self.first_produc_hoodies).click()

    def click_in_mode_list(self):
        self.driver.find_element(By.ID, self.id_modeList).click()

    def the_mode_was_changed_to_list(self):
        isDisplayed = self.driver.find_element(By.XPATH, self.xpath_view_mode_list).get_attribute('className').__eq__(self.class_view_mode_list)
        list_product = self.driver.find_elements(By.CLASS_NAME, self.first_produc_hoodies)
        return isDisplayed and list_product.__len__() != 0

    def click_sort_by_price(self):
        self.driver.find_element(By.ID, self.id_sorter_list).click()
        self.driver.find_element(By.XPATH, self.xpath_order_by_price).click()

    def verify_url(self, url):
        return self.driver.current_url == url







