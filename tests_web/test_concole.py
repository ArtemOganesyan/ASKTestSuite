
import pytest

import config
from web.web_common import WebCommonMethods
from utilities import logger
from utilities.test_data import get_test_data
from pom.common_page import CommonPage


class TestConsole:
    logger = logger.get_logger()

    # loads page with console log events not SEVERE
    @pytest.mark.skip
    def test_console_log_positive(self, setup):
        driver = setup[0]
        driver.get("https://pepsi.com")
        self.logger.debug("asserting browser console log")
        assert WebCommonMethods.b_log_checker(driver.get_log('browser'))

    # loads page with console log events SEVERE
    @pytest.mark.skip
    def test_console_log_negative(self, setup):
        driver = setup[0]
        driver.get("http://foo.com")
        self.logger.debug("asserting browser console log")
        assert WebCommonMethods.b_log_checker(driver.get_log('browser'))