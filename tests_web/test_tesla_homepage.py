import pytest
from utilities import logger
from utilities.test_data import get_test_data
from pom.tesla_home_page import HomePage


# this test suit verifies login form functionality for teacher and student users
class TestSignIn:
    logger = logger.get_logger()

    #  this test checks visibility of all web elements in different screen resolutions
    @pytest.mark.test
    def test_tesla_home_page_mac_air2(self, setup):
        self.logger.debug("invoking browser")
        driver = setup
        # this  creates object with attributes being instances of all application pages
        home_page = HomePage(driver)
        self.logger.debug("getting test data")
        test_data = get_test_data('responsive', 'TeslaHomePage', 'MacAir2')
        self.logger.debug(f"navigating to url: {home_page.page_url}")
        driver.get(home_page.page_url)
        self.logger.debug("setting window size")
        driver.set_window_size(test_data['w'], test_data['h'])

        # this loop will assert visibility of all home page elements
        for el in home_page.locators_list:
            # this check desktop only elements being tested for mobile resolutions
            if test_data['type'] in el[1]:
                self.logger.debug(f"getting element {el}")
                visibility = home_page.check_element_is_displayed(el)
                self.logger.debug("asserting element visibility")
                assert visibility, self.logger.error("element is not visible")


    def test_tesla_home_page_iphone14(self, setup):
        self.logger.debug("invoking browser")
        driver = setup
        # this  creates object with attributes being instances of all application pages
        home_page = HomePage(driver)
        self.logger.debug("getting test data")
        test_data = get_test_data('responsive', 'TeslaHomePage', 'iPhone14')
        self.logger.debug(f"navigating to url: {home_page.page_url}")
        driver.get(home_page.page_url)
        self.logger.debug("setting window size")
        driver.set_window_size(test_data['w'], test_data['h'])

        # this loop will assert visibility of all home page elements
        for el in home_page.locators_list:
            # this check desktop only elements being tested for mobile resolutions
            if test_data['type'] in el[1]:
                self.logger.debug(f"getting element {el}")
                visibility = home_page.check_element_is_displayed(el)
                self.logger.debug("asserting element visibility")
                assert visibility, self.logger.error("element is not visible")

    def test_tesla_home_page_imac24(self, setup):
        self.logger.debug("invoking browser")
        driver = setup
        # this  creates object with attributes being instances of all application pages
        home_page = HomePage(driver)
        self.logger.debug("getting test data")
        test_data = get_test_data('responsive', 'TeslaHomePage', 'iMac24')
        self.logger.debug(f"navigating to url: {home_page.page_url}")
        driver.get(home_page.page_url)
        self.logger.debug("setting window size")
        driver.set_window_size(test_data['w'], test_data['h'])

        # this loop will assert visibility of all home page elements
        for el in home_page.locators_list:
            # this check desktop only elements being tested for mobile resolutions
            if test_data['type'] in el[1]:
                self.logger.debug(f"getting element {el}")
                visibility = home_page.check_element_is_displayed(el)
                self.logger.debug("asserting element visibility")
                assert visibility, self.logger.error("element is not visible")

    def test_tesla_home_page_ipad_pro_12_9(self, setup):
        self.logger.debug("invoking browser")
        driver = setup
        # this  creates object with attributes being instances of all application pages
        home_page = HomePage(driver)
        self.logger.debug("getting test data")
        test_data = get_test_data('responsive', 'TeslaHomePage', 'iPadPro12.9')
        self.logger.debug(f"navigating to url: {home_page.page_url}")
        driver.get(home_page.page_url)
        self.logger.debug("setting window size")
        driver.set_window_size(test_data['w'], test_data['h'])

        # this loop will assert visibility of all home page elements
        for el in home_page.locators_list:
            # this check desktop only elements being tested for mobile resolutions
            if test_data['type'] in el[1]:
                self.logger.debug(f"getting element {el}")
                visibility = home_page.check_element_is_displayed(el)
                self.logger.debug("asserting element visibility")
                assert visibility, self.logger.error("element is not visible")










