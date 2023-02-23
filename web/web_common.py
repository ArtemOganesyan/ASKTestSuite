import os
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utilities.logger import get_logger
from allure_commons.types import AttachmentType
import allure



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

    # @staticmethod
    # def get_screenshot(driver, test_name):
    #     driver.save_screenshot(f"../screenshots/{test_name}_screenshot.png")

    @staticmethod
    # this method will return boolean
    def is_displayed(element):
        return element.is_displayed()

    # this method logs console errors and returns check results
    @staticmethod
    def b_log_checker(log):
        logger = get_logger()
        result = True
        # try/except to continue in case log is an empty list
        try:
            for el in log:
                if el['level'] == 'SEVERE':
                    logger.error(f'Browser Console Error: {el}')
                    result = False
        except:
            pass

        return result

    @staticmethod
    def take_screen_shot(test_name, driver):
        if not os.path.exists("./screenshots"):
            os.makedirs("./screenshots")

        # driver.save_screenshot(f"./screenshots/{test_name}.png")
        allure.attach(driver.get_screenshot_as_png(), name=f"{test_name}", attachment_type=AttachmentType.PNG)
        driver.quit()



