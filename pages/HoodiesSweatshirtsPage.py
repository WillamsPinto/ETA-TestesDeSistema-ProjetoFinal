from selenium.webdriver.common.by import By
from Helpers.session import Session

class HoodiesSweatshirtsPage(Session):

    primeiro_produto_hoodies = 'product-item-info'
    url = 'https://magento.softwaretestingboard.com/women/tops-women/hoodies-and-sweatshirts-women.html'
    text_HoodiesSweatshirts_title = "Hoodies & Sweatshirts"
    class_products_list = 'product-item-link'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def is_HoodiesSweatshirts_page(self):
        return self.is_page(self.url, self.text_HoodiesSweatshirts_title)

    def salvar_nome_produto(self):
        lista_produtos = self.driver.find_elements(By.CLASS_NAME, self.class_products_list)
        return lista_produtos[0].text


    def clicar_primeiro_produto_hoddies(self):
        self.driver.find_element(By.CLASS_NAME, self.primeiro_produto_hoodies).click()
