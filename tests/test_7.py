
import pytest

from pages.SearchPage import SearchPage


class Test7:

    @pytest.mark.suite7
    @pytest.mark.parametrize('all_browsers', ['chrome'])
    def test_search_product(self, open_home_all_browsers):
        item = 'jacket'
        home_page = open_home_all_browsers
        home_page.open_home_page()
        home_page.insert_item_in_searchbar(item)
        home_page.click_enter()
        search_page = SearchPage(home_page.driver)
        assert search_page.is_search_result_page(item),'Não é a página de Resultados'
        assert search_page.is_check_product_name(item)

