import pytest

from pages.ProductPage import ProductPage
from pages.ShoppingCartPage import ShoppingCartPage


class Test11:

    @pytest.mark.suite10
    @pytest.mark.parametrize('all_browsers', ['chrome'])
    def test_select_product_to_compare(self, open_home_all_browsers):
        home_page = open_home_all_browsers
        home_page.open_home_page()
        first_product_name = home_page.get_first_product_name()
        home_page.click_first_product()
        product_page = ProductPage(home_page.driver)
        assert product_page.is_product_page(first_product_name), "Não foi direcionado para a página do produto"
        product_page.click_in_xs_size()
        assert product_page.xs_size_was_selected(), "O tamanho xs não foi selecionado"
        product_page.click_in_blue_color()
        assert product_page.blue_color_was_selected(), "A primeira cor não foi selecionada"
        product_page.insert_quant_value(5)
        product_page.click_in_add_button()
        product_page.click_in_cart_icon()
        product_page.click_in_view_cart_link()
        shoppingCart_Page = ShoppingCartPage(product_page.driver)
        assert shoppingCart_Page.is_ShoppingCartPage_page(), "Não foi direcionado para a página do carrinho"