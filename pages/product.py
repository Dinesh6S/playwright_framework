import logging
import time
class Product:
    def __init__(self, driver):
        self.driver = driver

    def open_produce(self):
        product_map = {}
        logging.info("finding product link")
        with self.driver.expect_popup() as page1_info:
            self.driver.locator('//div[@data-cy="title-recipe"]//a[@target="_blank"]').nth(3).click()
        logging.info("product link clicked successfully")
        time.sleep(3)
        page1 = page1_info.value
        product_title = page1.locator('//span[@id="productTitle"]').text_content()
        product_price = page1.locator('//span[@class="aok-offscreen"]').text_content()
        product_map['name'] = product_title.strip()
        product_map['price'] = product_price.split(' with')[0].replace('₹', '').strip()
        logging.info("finding add to cart button")
        page1.get_by_role("button", name="Add to Cart").click()
        logging.info("Add to cart button clicked successfully")
        logging.info("finding cary details tab close button")
        page1.get_by_label("Exit this panel and return to").click()
        logging.info("Cart details tab closed successfully")
        page1.close()
        return product_map