import logging
import time


class Home:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        logging.info("Browser Opened successfully")
        self.driver.goto(url)
        logging.info("Website Opened successfully")
