from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

from Helpers.session import Session


class HomePage(Session):
    url = 'https://magento.softwaretestingboard.com/'
    xpath_createAccountLink = '/html/body/div[1]/header/div[1]/div/ul/li[3]/a'
    id_whatsnew = 'ui-id-3'
    id_searchbar = 'search'
    xpath_shopNewYoga_btn = '//*[@id="maincontent"]/div[3]/div/div[2]/div[1]/a/span/span[2]'

    def __init__(self, browser):
        super().__init__(browser=browser)
        self.open_home_page()

    def open_home_page(self):
        self.driver.get(self.url)

    def is_home_page(self):
        return self.driver.current_url == self.url

    def click_in_create_account_link(self):
        self.driver.find_element(By.XPATH, self.xpath_createAccountLink).click()

    def click_in_whatsnew(self):
        self.driver.find_element(By.ID, self.id_whatsnew).click()

    def insert_item_in_searchbar(self, item):
        self.driver.find_element(By.ID, self.id_searchbar).send_keys(item)

    def click_enter(self):
        self.driver.find_element(By.ID, self.id_searchbar).send_keys(Keys.ENTER)

    def click_shop_new_yoga_option(self):
        time.sleep(2.5)
        self.driver.find_element(By.XPATH, self.xpath_shopNewYoga_btn).click()
