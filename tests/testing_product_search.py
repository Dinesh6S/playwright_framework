import time
import pytest
import conftest

def test_product_add_to_cart(pages):
    pages.home.navigate(conftest.config.get('base_url'))
    pages.search.search_produce('apple watch')
    product_details = pages.product.open_produce()
    print(product_details)
    pages.search.search_produce('apple phone')
    product_details = pages.product.open_produce()
    print(product_details)
