import time
from selenium.webdriver.common.by import By
from Helpers.session import Session


class MyAccountPage(Session):
    url = 'https://magento.softwaretestingboard.com/customer/account/'
    text_MyAccount_title = 'My Account'
    text_success_message_register = 'Thank you for registering with Main Website Store.'
    xpath_success_message = '//*[@id="maincontent"]/div[1]/div[2]/div/div/div'
    xpath_contactInformation_boxContent = '//*[@id="maincontent"]/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/p'
    xpath_welcome_menu = '/html/body/div[1]/header/div[1]/div/ul/li[1]'
    welcome_text = 'Welcome'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_myAccount_page(self):
        return self.is_page(self.url, self.text_MyAccount_title)

    def has_success_message_registration(self):
        time.sleep(2.5)
        message = self.driver.find_element(By.XPATH, self.xpath_success_message).text
        return message == self.text_success_message_register

    def has_contact_information(self, firstName, lastName, email):
        message = self.driver.find_element(By.XPATH, self.xpath_contactInformation_boxContent).text
        return f"{firstName} {lastName}\n{email}".__eq__(message)

    def has_welcome_menu(self, firstName, lastName):
        message = self.driver.find_element(By.XPATH, self.xpath_welcome_menu).text
        return f"{self.welcome_text}, {firstName} {lastName}!".__eq__(message)
