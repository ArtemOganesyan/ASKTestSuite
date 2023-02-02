import pytest
import config
import json
import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as GeckoService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utilities.logger import get_logger
from selenium.webdriver.safari.options import Options as SafariOptions


@pytest.fixture
def setup(request):
    logger = get_logger()
    browser_name = request.config.getoption("browser")
    if browser_name == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        return driver

    elif browser_name == 'firefox':
        driver = webdriver.Firefox(service=GeckoService(GeckoDriverManager().install()))
        driver.maximize_window()
        return driver

    elif browser_name == 'safari':

        driver = webdriver.Safari(options=SafariOptions())
        driver.maximize_window()
        return driver

    else:
        error_message = 'browser name error or browser is not supported'
        logger.error(error_message)
        raise ValueError(error_message)


#  this function adds cross-browser functionality
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
