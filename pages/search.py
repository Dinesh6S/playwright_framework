import logging


class Search:
    def __init__(self, driver):
        self.driver = driver

    def search_produce(self, product_name):
        logging.info("Search field clicked successfully")
        self.driver.get_by_placeholder("Search Amazon.in").click()
        logging.info("Finding Search input Element")
        self.driver.get_by_placeholder("Search Amazon.in").fill(product_name)
        logging.info("entered porduce name successfully")
        logging.info("finding search button")
        self.driver.locator('//input[@id="nav-search-submit-button"]').click()
        logging.info("search button clicked successfully")