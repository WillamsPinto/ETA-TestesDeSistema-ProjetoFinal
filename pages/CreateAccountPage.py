import time
from selenium.webdriver.common.by import By
from Helpers.session import Session

class CreateAccountPage(Session):
    url = 'https://magento.softwaretestingboard.com/customer/account/create/'
    text_CreateAccount_title = 'Create New Customer Account'
    id_FirstName_TextField = 'firstname'
    id_LastName_TextField = 'lastname'
    id_Email_TextField = "email_address"
    id_Password_TextField = 'password'
    id_PasswordConfirmation_TextField = 'password-confirmation'
    xpath_CreateAccount_btn = '//*[@id="form-validate"]/div/div[1]/button'
    text_error_message_account_already_exists = "There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account."
    xpath_page_messages = '//*[@id="maincontent"]/div[2]/div[2]/div/div/div'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_createAccount_page(self):
        return self.is_page(self.url, self.text_CreateAccount_title)

    def fill_all_textField(self, firstName, lastName, email, password, confirmPassword):
        self.fill_the_firstName(firstName)
        self.fill_the_lastName(lastName)
        self.fill_the_email(email)
        self.fill_the_password(password)
        self.fill_the_confirm_password(confirmPassword)

    def fill_the_firstName(self, firstName):
        self.driver.find_element(By.ID, self.id_FirstName_TextField).send_keys(firstName)

    def fill_the_lastName(self, lastName):
        self.driver.find_element(By.ID, self.id_LastName_TextField).send_keys(lastName)

    def fill_the_email(self, email):
        self.driver.find_element(By.ID, self.id_Email_TextField).send_keys(email)

    def fill_the_password(self, password):
        self.driver.find_element(By.ID, self.id_Password_TextField).send_keys(password)

    def fill_the_confirm_password(self, confirmPassword):
        self.driver.find_element(By.ID, self.id_PasswordConfirmation_TextField).send_keys(confirmPassword)

    def click_in_createAccount_button(self):
        self.driver.find_element(By.XPATH, self.xpath_CreateAccount_btn).click()

    def has_error_message_account_already_exists(self):
        time.sleep(2.5)
        error_msg = self.driver.find_element(By.XPATH, self.xpath_page_messages).text
        return error_msg == self.text_error_message_account_already_exists