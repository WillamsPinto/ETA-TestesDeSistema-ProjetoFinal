import pytest
from pages.HoodiesSweatshirtsPage import HoodiesSweatshirtsPage
from pages.WhatsNewPage import WhatsNewPage


class Test8:

    @pytest.mark.suite8
    @pytest.mark.parametrize('all_browsers', ['chrome'])
    def test_change_product_display_to_list_mode(self, open_home_all_browsers):
        home_page = open_home_all_browsers
        home_page.open_home_page()
        home_page.click_in_whatsnew()
        whatsNew_page = WhatsNewPage(home_page.driver)
        assert whatsNew_page.is_whatsnew_page(), "Não foi direcionado para o whats new"
        whatsNew_page.click_first_item_menu_hoddies()
        hoodiesSweatshirts_page = HoodiesSweatshirtsPage(whatsNew_page.driver)
        assert hoodiesSweatshirts_page.is_HoodiesSweatshirts_page(), "Não foi direcionado para a página Hoodies & Sweatshirts"
        hoodiesSweatshirts_page.click_in_mode_list()
        assert hoodiesSweatshirts_page.the_mode_was_changed_to_list(), "A visualização não foi trocada ou não existe item na lista"
