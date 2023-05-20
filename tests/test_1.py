import pytest

from pages.CreateAccountPage import CreateAccountPage


class Test1:

    @pytest.mark.suite1
    @pytest.mark.parametrize('all_browsers', ['chrome'])
    def test_realizar_cadastro_do_usuario_com_email_ja_existente(self, open_home_all_browsers):
        home_page = open_home_all_browsers
        home_page.open_home_page()
        assert home_page.is_home_page(), 'Página não encontrada!'
        home_page.click_in_create_account_link()
        createAccount_Page = CreateAccountPage(driver=home_page.driver)
        assert createAccount_Page.is_createAccount_page(), 'Página não redirecionada encontrada!'
        createAccount_Page.fill_all_textField('Jose', 'Silva', 'roni_cost@example.com', 'teste@123', 'teste@123')
        createAccount_Page.click_in_createAccount_button()
        assert createAccount_Page.has_error_message_account_already_exists(), "Mensagem Incorreta!"
        assert createAccount_Page.is_createAccount_page(), "O usuário foi redirecionado para outra página!"
