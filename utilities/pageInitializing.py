from pages.home import Home
from pages.product import Product
from pages.search import Search


class PageInitializer:
    def __init__(self, driver, env):
        self.home = Home(driver)
        self.search = Search(driver)
        self.product = Product(driver)



