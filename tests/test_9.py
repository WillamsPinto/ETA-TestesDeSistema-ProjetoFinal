import pytest
from pages.HoodiesSweatshirtsPage import HoodiesSweatshirtsPage
from pages.WhatsNewPage import WhatsNewPage
class Test9:

    @pytest.mark.suite9
    @pytest.mark.parametrize('all_browsers', ['chrome'])
    def test_order_by_price(self, open_home_all_browsers):
        home_page = open_home_all_browsers
        home_page.open_home_page()
        home_page.click_in_whatsnew()
        whatsNew_page = WhatsNewPage(home_page.driver)
        assert whatsNew_page.is_whatsnew_page(), "Não foi direcionado para o whats new"
        whatsNew_page.click_first_item_menu_hoddies()
        hoodiesSweatshirts_page = HoodiesSweatshirtsPage(home_page.driver)
        assert hoodiesSweatshirts_page.is_HoodiesSweatshirts_page(), "Não foi direcionado para a página Hoodies & Sweatshirts"
        hoodiesSweatshirts_page.click_sort_by_price()
        assert hoodiesSweatshirts_page.verify_url(hoodiesSweatshirts_page.url_by_price), "Não foi direcionado para filtro por preço"