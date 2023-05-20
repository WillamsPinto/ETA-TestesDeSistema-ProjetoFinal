from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Helpers.session import Session


class SearchPage(Session):
    Url='https://magento.softwaretestingboard.com/catalogsearch/result/?q='
    SearchResultTitle = "Search results for: 'item'"
    class_products_list = 'product-item-link'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_search_result_page(self, item):
        newUrl = f"{self.Url}{item}".replace(" ", "+")
        newSearchResultTitle = self.SearchResultTitle.replace('item', item)
        return self.is_page(newUrl.lower(), newSearchResultTitle)

    def is_check_product_name(self,item):
        product_list = self.driver.find_elements(By.CLASS_NAME, self.class_products_list)
        return product_list[0].text.lower().__contains__(item)


