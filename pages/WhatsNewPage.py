from selenium.webdriver.common.by import By
from Helpers.session import Session

class WhatsNewPage(Session):

    xpath_first_item_menu_hoodies = '//*[@id="maincontent"]/div[4]/div[2]/div/div/ul[1]/li[1]/a'
    url = 'https://magento.softwaretestingboard.com/what-is-new.html'
    text_whatsnew_title = "What's New"

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_whatsnew_page(self):
        return self.is_page(self.url, self.text_whatsnew_title)

    def click_first_item_menu_hoddies(self):
        self.driver.find_element(By.XPATH, self.xpath_first_item_menu_hoodies).click()
