import pytest
from pages.NewLumaYogaPage import NewLumaYoga
from pages.ProductComparePage import ProductComparePage
from pages.ProductPage import ProductPage

class Test10:

    @pytest.mark.suite10
    @pytest.mark.parametrize('all_browsers', ['chrome'])
    def test_select_product_to_compare(self, open_home_all_browsers):
        home_page = open_home_all_browsers
        home_page.open_home_page()
        home_page.click_shop_new_yoga_option()
        newLumaYoga_page = NewLumaYoga(home_page.driver)
        assert newLumaYoga_page.is_newLumaYoga_page(), "Não foi direcionado para a página New Luma Yoga Collection"
        first_product = newLumaYoga_page.get_first_product_name()
        newLumaYoga_page.click_first_product_newLumaYoga()
        product_page = ProductPage(newLumaYoga_page.driver)
        assert product_page.is_product_page(first_product), "Não foi direcionado para a página do produto"
        product_page.click_in_compare_option()
        assert product_page.has_add_product_in_compare_list_successfully(), "A mensagem de sucesso não foi exibida"
        product_page.click_in_compare_list_link()
        productCompare_page = ProductComparePage(product_page.driver)
        assert productCompare_page.is_compare_page(), "Não foi direcionado para a página de comparação"
        assert productCompare_page.has_product_in_page(first_product), "Não foi encontrado item na página de comparação"