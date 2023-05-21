import pytest

from pages.WhatsNewPage import WhatsNewPage
from pages.HoodiesSweatshirtsPage import HoodiesSweatshirtsPage
from pages.ProductPage import ProductPage


class Test6:

    @pytest.mark.suite6
    @pytest.mark.parametrize('all_browsers', ['chrome'])
    def test_add_product_to_cart(self, open_home_all_browsers):
            home_page = open_home_all_browsers
            home_page.open_home_page()
            home_page.click_in_whatsnew()
            whatsnew_page = WhatsNewPage(home_page.driver)
            assert whatsnew_page.is_whatsnew_page(), "Página não encontrada!"
            whatsnew_page.click_first_item_menu_hoddies()
            hoodiesSweatshirts_page = HoodiesSweatshirtsPage(whatsnew_page.driver)
            assert hoodiesSweatshirts_page.is_HoodiesSweatshirts_page(), "Página não encontrada!"
            nome_primeiro_produto_hoodies = hoodiesSweatshirts_page.get_product_name()
            hoodiesSweatshirts_page.click_first_product_hoddies()
            product_page = ProductPage(hoodiesSweatshirts_page.driver)
            assert product_page.is_product_page(nome_primeiro_produto_hoodies)
            product_page.add_product_in_cart()
            assert product_page.has_success_message_product_to_cart(), "Produto não adicionado ao carrinho!"
            assert product_page.has_product_added_to_cart('1'), "Valor do carrinho diferente de 1!"
