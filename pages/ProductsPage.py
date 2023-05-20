from random import randint

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from Helpers.session import Session


class ProductsPage(Session):

    url = 'https://www.saucedemo.com/inventory.html'
    text_product_title = 'Products'
    class_product_item = 'inventory_item'
    id_menu = 'react-burger-menu-btn'
    class_product_item = 'inventory_item'
    tag_add_to_cart_btn = 'button'
    class_shopping_cart_badge = 'shopping_cart_badge'
    class_shopping_cart_icon = 'shopping_cart_link'
    class_product_name = 'inventory_item_name'
    txt_remove_btn = 'Remove'
    class_product_filter = 'product_sort_container'
    value_filter_item_price_low_to_high = "[value='lohi']"
    class_item_price = 'inventory_item_price'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_products_page(self):
        return self.is_page(self.url, self.text_product_title)

    def count_products_page(self):
        count_products = len(self.driver.find_elements(By.CLASS_NAME, self.class_product_item))
        return count_products

    def has_menu_btn(self):
        try:
            self.driver.find_element(By.ID, self.id_menu)
            return True
        except NoSuchElementException:
            return False

    def add_first_product_to_cart(self):
        product_list_elements = self.driver.find_elements(By.CLASS_NAME, self.class_product_item)
        product_list_elements[0].find_element(By.TAG_NAME, self.tag_add_to_cart_btn).click()
        cart_number = self.get_cart_number()
        if cart_number != "1":
            raise Exception("Carrinho não contem 1 produto!")
        return product_list_elements[0].find_element(By.CLASS_NAME, self.class_product_name).text

    def get_cart_number(self):
        return self.driver.find_element(By.CLASS_NAME, self.class_shopping_cart_badge).text

    def add_random_product_to_cart(self):
        product_list_elements = self.driver.find_elements(By.CLASS_NAME, self.class_product_item)
        random_product = randint(0, len(product_list_elements) - 1)
        random_product_card = product_list_elements[random_product]
        random_product_card.find_element(By.TAG_NAME, self.tag_add_to_cart_btn).click()
        button_text = random_product_card.find_element(By.TAG_NAME, self.tag_add_to_cart_btn).text
        if button_text != self.txt_remove_btn:
            raise Exception('Botão não mudou para REMOVE!')
        return random_product_card.find_element(By.CLASS_NAME, self.class_product_name).text

    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME, self.class_shopping_cart_icon).click()

    def filter_by_price_low_to_high(self):
        self.driver.find_element(By.CLASS_NAME, self.class_product_filter).click()
        self.driver.find_element(By.CSS_SELECTOR, self.value_filter_item_price_low_to_high).click()

    def check_order_low_to_high(self):
        all_item_price = self.driver.find_elements(By.CLASS_NAME, self.class_item_price)

        for i in range(len(all_item_price) - 1):
            current_price = float(all_item_price[i].text.replace('$', ''))
            next_price = float(all_item_price[i + 1].text.replace('$', ''))
            if current_price > next_price:
                return False
        return True
