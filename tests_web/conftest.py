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
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as GeckoOptions


@pytest.fixture(scope="function")
def setup(request):

    logger = get_logger()
    browser_name = request.config.getoption("browser")
    browser_mode = request.config.getoption("mode")

    logger.debug(f"invoking browser {browser_name} in {browser_mode} mode")
    if browser_name == 'chrome':
        options = ChromeOptions()
        if browser_mode == 'headless':
            options.headless = True
        else:
            options.headless = False

        # enabling browser console log
        dc = DesiredCapabilities.CHROME
        dc['loggingPrefs'] = {'browser': 'ALL'}

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), desired_capabilities=dc,
                                  options=options)

        driver.maximize_window()
        yield driver, browser_name
        logger.debug(f"killing browser {browser_name} ")
        driver.quit()

    elif browser_name == 'firefox':
        options = GeckoOptions()
        if browser_mode == 'headless':
            options.headless = True
        else:
            options.headless = False

        # browser logs now working for firefox
        dc = DesiredCapabilities.FIREFOX
        dc['loggingPrefs'] = {'browser': 'ALL'}
        driver = webdriver.Firefox(service=GeckoService(GeckoDriverManager().install()), desired_capabilities=dc,
                                   options=options)
        driver.maximize_window()
        yield driver, browser_name
        logger.debug(f"killing browser {browser_name} ")
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
    parser.addoption("--mode", action="store", default="regular")
