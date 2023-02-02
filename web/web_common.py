from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# this class contains common webdriver methods that can be reused in POM action methods
class WebCommonMethods:
    @staticmethod
    def get_element(driver, locator):
        el = driver.find_element(*locator)
        return el

    @staticmethod
    def click_element(element):
        element.click()

    @staticmethod
    def input_field(element, text):
        element.send_keys(text)

    @staticmethod
    def get_text(element):
        text = element.text
        return text

    @staticmethod
    def wait_for_element_visibility(locator, timeout, driver):
        wait = WebDriverWait(driver, timeout)
        wait.until(ec.visibility_of_element_located(locator))

