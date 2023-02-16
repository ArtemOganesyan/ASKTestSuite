"""
Updated: tesla test logic, driver.quit() added, browser name is now logged, boundary tests added

Issues:

* Tesla remaining screens

html is dynamically generated, same path to different screens
//*[@id='block-tesla-frontend-content']/div/section/div/div/div/section/a


* Safari crashes (ASK)
* Safari won't close (teardown)
* Waits
* GitIgnore


2do:
* Tesla remaining screens

"""

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
from pom.common_page import CommonPage

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
page = CommonPage(driver)
driver.implicitly_wait(3)
driver.get('http://ask-qa.portnov.com/#/login')
page.sign_in_page.fill_out_email_field('student1@gmail.com')
page.sign_in_page.fill_out_password_field('12345')
page.sign_in_page.click_submit_button()
cookies = driver.get_cookies()
print(cookies)








