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
        driver = setup
        # this  creates object with attributes being instances of all application pages
        home_page = HomePage(driver)
        self.logger.debug("getting test data")
        test_data = get_test_data('responsive', 'TeslaHomePage', 'MacAir2')
        self.logger.debug(f"navigating to url: {home_page.page_url}")
        driver.get(home_page.page_url)
        self.logger.debug(f"setting window size to {test_data['w'], test_data['h']}")
        driver.set_window_size(test_data['w'], test_data['h'])

        # this list contains visibility boolean for each element
        test_results = []
        # this loop asserts visibility of all home page elements
        for el in home_page.locators_list:
            # this checks if element should be visible in test resolution
            if test_data['type'] in el[1]:
                try:
                    self.logger.debug(f"asserting  visibility of {el}")
                    visibility = home_page.check_element_is_displayed(el)
                    test_results.append(visibility)
                except:
                    self.logger.error("element is not visible")
                    test_results.append(False)

        self.logger.debug("asserting test results")
        if False in test_results:
            assert False
        else:
            assert True

    def test_tesla_home_page_iphone14(self, setup):
        driver = setup
        # this  creates object with attributes being instances of all application pages
        home_page = HomePage(driver)
        self.logger.debug("getting test data")
        test_data = get_test_data('responsive', 'TeslaHomePage', 'iPhone14')
        self.logger.debug(f"navigating to url: {home_page.page_url}")
        driver.get(home_page.page_url)
        self.logger.debug(f"setting window size to {test_data['w'], test_data['h']}")
        driver.set_window_size(test_data['w'], test_data['h'])

        # this list contains visibility boolean for each element
        test_results = []
        # this loop asserts visibility of all home page elements
        for el in home_page.locators_list:
            # this checks if element should be visible in test resolution
            if test_data['type'] in el[1]:
                try:
                    self.logger.debug(f"asserting  visibility of {el}")
                    visibility = home_page.check_element_is_displayed(el)
                    test_results.append(visibility)
                except:
                    self.logger.error("element is not visible")
                    test_results.append(False)

        self.logger.debug("asserting test results")
        if False in test_results:
            assert False
        else:
            assert True

    def test_tesla_home_page_imac24(self, setup):
        driver = setup
        # this  creates object with attributes being instances of all application pages
        home_page = HomePage(driver)
        self.logger.debug("getting test data")
        test_data = get_test_data('responsive', 'TeslaHomePage', 'iMac24')
        self.logger.debug(f"navigating to url: {home_page.page_url}")
        driver.get(home_page.page_url)
        self.logger.debug(f"setting window size to {test_data['w'], test_data['h']}")
        driver.set_window_size(test_data['w'], test_data['h'])

        # this list contains visibility boolean for each element
        test_results = []
        # this loop asserts visibility of all home page elements
        for el in home_page.locators_list:
            # this checks if element should be visible in test resolution
            if test_data['type'] in el[1]:
                try:
                    self.logger.debug(f"asserting  visibility of {el}")
                    visibility = home_page.check_element_is_displayed(el)
                    test_results.append(visibility)
                except:
                    self.logger.error("element is not visible")
                    test_results.append(False)

        self.logger.debug("asserting test results")
        if False in test_results:
            assert False
        else:
            assert True

    def test_tesla_home_page_ipad_pro_12_9(self, setup):
        driver = setup
        # this  creates object with attributes being instances of all application pages
        home_page = HomePage(driver)
        self.logger.debug("getting test data")
        test_data = get_test_data('responsive', 'TeslaHomePage', 'iPadPro12.9')
        self.logger.debug(f"navigating to url: {home_page.page_url}")
        driver.get(home_page.page_url)
        self.logger.debug(f"setting window size to {test_data['w'], test_data['h']}")
        driver.set_window_size(test_data['w'], test_data['h'])

        # this list contains visibility boolean for each element
        test_results = []
        # this loop asserts visibility of all home page elements
        for el in home_page.locators_list:
            # this checks if element should be visible in test resolution
            if test_data['type'] in el[1]:
                try:
                    self.logger.debug(f"asserting  visibility of {el}")
                    visibility = home_page.check_element_is_displayed(el)
                    test_results.append(visibility)
                except:
                    self.logger.error("element is not visible")
                    test_results.append(False)

        self.logger.debug("asserting test results")
        if False in test_results:
            assert False
        else:
            assert True

    # this tests asserts on high boundary w 1200 all desktop elements are visible
    @pytest.mark.boundary
    def test_tesla_home_page_boundary_high(self, setup):
        driver = setup
        # this  creates object with attributes being instances of all application pages
        home_page = HomePage(driver)
        self.logger.debug("getting test data")
        test_data = get_test_data('responsive', 'TeslaHomePage', 'BoundaryHigh')
        self.logger.debug(f"navigating to url: {home_page.page_url}")
        driver.get(home_page.page_url)
        self.logger.debug(f"setting window size to {test_data['w'], test_data['h']}")
        driver.set_window_size(test_data['w'], test_data['h'])

        # this list contains visibility boolean for each element
        test_results = []
        # this loop asserts visibility of all home page elements
        for el in home_page.locators_list:
            # this checks if element should be visible in test resolution
            if test_data['type'] in el[1]:
                try:
                    self.logger.debug(f"asserting  visibility of {el}")
                    visibility = home_page.check_element_is_displayed(el)
                    test_results.append(visibility)
                except:
                    self.logger.error("element is not visible")
                    test_results.append(False)

        self.logger.debug("asserting test results")
        if False in test_results:
            assert False
        else:
            assert True

    # this tests asserts on low boundary w 1119 all mobile elements are visible
    @pytest.mark.boundary
    def test_tesla_home_page_boundary_low(self, setup):
        driver = setup
        # this  creates object with attributes being instances of all application pages
        home_page = HomePage(driver)
        self.logger.debug("getting test data")
        test_data = get_test_data('responsive', 'TeslaHomePage', 'BoundaryLow')
        self.logger.debug(f"navigating to url: {home_page.page_url}")
        driver.get(home_page.page_url)
        self.logger.debug(f"setting window size to {test_data['w'], test_data['h']}")
        driver.set_window_size(test_data['w'], test_data['h'])

        # this list contains visibility boolean for each element
        test_results = []
        # this loop asserts visibility of all home page elements
        for el in home_page.locators_list:
            # this checks if element should be visible in test resolution
            if test_data['type'] in el[1]:
                try:
                    self.logger.debug(f"asserting  visibility of {el}")
                    visibility = home_page.check_element_is_displayed(el)
                    test_results.append(visibility)
                except:
                    self.logger.error("element is not visible")
                    test_results.append(False)

        self.logger.debug("asserting test results")
        if False in test_results:
            assert False
        else:
            assert True
