import random
import string

import pytest
from pages.CreateAccountPage import CreateAccountPage
from pages.MyAccountPage import MyAccountPage


class Test2:

    @pytest.mark.suite2
    @pytest.mark.parametrize('all_browsers', ['chrome'])
    def test_realizar_cadastro_de_novo_usuario(self, open_home_all_browsers):
        #Arrange
        firstName = 'Jose'
        lastName = 'Silva'
        password = 'teste@123'
        confirmPassword = 'teste@123'
        home_page = open_home_all_browsers
        home_page.open_home_page()
        assert home_page.is_home_page(), 'Página não encontrada!'
        home_page.click_in_create_account_link()
        createAccount_Page = CreateAccountPage(driver=home_page.driver)
        assert createAccount_Page.is_createAccount_page(), 'Página não redirecionada!'

        #Act
        suffixLength = 10
        generatedSuffix = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(suffixLength))
        generatedAddress = f"roni_cost{generatedSuffix}@example.com"
        createAccount_Page.fill_all_textField(firstName, lastName, generatedAddress, password, confirmPassword)
        createAccount_Page.click_in_createAccount_button()

        #Assert
        myAccount_page = MyAccountPage(createAccount_Page.driver)
        assert myAccount_page.is_myAccount_page(), 'Usuário não foi redirecionado!'
        assert myAccount_page.has_success_message_registration(), "Mensagem diferente do esperado!"
        assert myAccount_page.has_welcome_menu(firstName, lastName), "Menssagem de saudação incorreta!"
        assert myAccount_page.has_contact_information(firstName, lastName, generatedAddress), "Nome e e-mail difere do cadastrado!"
