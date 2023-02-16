import pytest
from selenium.webdriver import DesiredCapabilities

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
    logger.debug(f"invoking browser {browser_name}")
    if browser_name == 'chrome':
        # enabling browser console log
        dc = DesiredCapabilities.CHROME
        dc['loggingPrefs'] = {'browser': 'ALL'}
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), desired_capabilities=dc)

        driver.maximize_window()
        yield driver
        driver.quit()

    elif browser_name == 'firefox':
        # browser logs now working for firefox
        dc = DesiredCapabilities.FIREFOX
        dc['loggingPrefs'] = {'browser': 'ALL'}
        driver = webdriver.Firefox(service=GeckoService(GeckoDriverManager().install()), desired_capabilities=dc)
        driver.maximize_window()
        yield driver
        driver.quit()

    elif browser_name == 'safari':

        driver = webdriver.Safari(options=SafariOptions())
        driver.maximize_window()
        yield driver
        driver.quit()

    else:
        error_message = 'browser name error or browser is not supported'
        logger.error(error_message)
        raise ValueError(error_message)


#  this function adds cross-browser functionality
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
