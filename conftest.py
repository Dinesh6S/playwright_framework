# conftest.py
import os

import pytest
import yaml
import logging
from playwright.sync_api import sync_playwright
from utilities.pageInitializing import PageInitializer

env = ''

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("test.log", mode="w"),
        logging.StreamHandler()
    ]
)

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def driver(browser):
    # context = browser.new_context(viewport={"width": 1600, "height": 800})
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    driver = context.new_page()
    yield driver
    context.tracing.stop(path="trace.zip")
    context.close()

@pytest.fixture(scope="function")
def pages(driver):
    return PageInitializer(driver, env)


@pytest.fixture(scope='session', autouse=True)
def load_config(request):
    global config, env
    env = request.config.getoption("--ENV")
    CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config', f"{env}.yaml")
    with open(CONFIG_PATH) as config_file:
        config = yaml.safe_load(config_file)
    print(config)
    print('--config--')
    return config



def pytest_addoption(parser):
    parser.addoption(
        "--ENV",
        action="store",
        default="prod",
        help="An example runtime argument"
    )
