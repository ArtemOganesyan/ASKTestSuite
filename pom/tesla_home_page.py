from selenium.webdriver.common.by import By
from selenium import webdriver
from web.web_common import WebCommonMethods as Common


# this class contains Tesla HomePage web elements and methods
class HomePage:
    page_url = 'https://www.tesla.com/'

    # all = all resolutions, desktop = desktop only
    top_line_offer = [(By.CSS_SELECTOR, ".tcl-simple-banner"), 'desk_tab_mob']
    top_line_offer_learn_more_link = [(By.CSS_SELECTOR, "a[href='/support/incentives']"), 'desk_tab_mob']

    # header
    footer_logo = [(By.CSS_SELECTOR, ".tds-icon-logo-wordmark"), 'desk_tab_mob']
    footer_model_s_link = [(By.CSS_SELECTOR, "a[title= 'Model S']"), 'desk']
    footer_model_3_link = [(By.CSS_SELECTOR, "a[title= 'Model 3']"), 'desk']
    footer_model_Y_link = [(By.CSS_SELECTOR, "a[title= 'Model Y']"), 'desk']
    footer_model_X_link = [(By.CSS_SELECTOR, "a[title= 'Model X']"), 'desk']
    footer_Roof_link = [(By.CSS_SELECTOR, "a[title = 'Solar Roof']"), 'desk']
    footer_Panels_link = [(By.CSS_SELECTOR, "a[title = 'Solar Panels']"), 'desk']
    footer_shop_link = [(By.CSS_SELECTOR, "a[title = 'Shop']"), 'desk']
    footer_account_link = [(By.CSS_SELECTOR, "a[title = 'Account']"), 'desk']
    footer_menu_button = [(By.CSS_SELECTOR, "button[title = 'Menu']"), 'desk_tab_mob']

    # model 3 screen
    header_model_3 = [(By.XPATH, "(//h1[contains(text() , 'Model 3')])[1]"), "desk_tab_mob"]
    para_model_3_d = [(By.XPATH, "(//p[contains(@class, '-desktop')][contains(@style,'--tcl-homepage-hero')])[1]"), "desk_tab"]
    para_model_3_m = [(By.XPATH, "(//p[contains(@class, '-mobile')][contains(@style,'--tcl-homepage-hero')])[1]"), "mob"]

    # model 3 desk buttons
    button_order_model_3_d = [(By.XPATH, "(//div[contains(@class, '__buttons-on-desktop')])[1]/section/a[@title='Custom Order']"), "desk_tab"]
    button_demo_model_3_d = [(By.XPATH, "(//div[contains(@class, '__buttons-on-desktop')])[1]/section/a[@title='Demo Drive']"), "desk_tab"]
    # model 3 mobile buttons
    button_order_model_3_m = [(By.XPATH, "(//div[contains(@class, '__buttons-on-mobile')])[1]/section/a[@title='Custom Order']"), "mob"]
    button_demo_model_3_m = [(By.XPATH, "(//div[contains(@class, '__buttons-on-mobile')])[1]/section/a[@title='Demo Drive']"), "mob"]
    img = [(By.XPATH, "//*[@id='tesla-hero-parallax-1873']/div/picture/img"), "desk_tab_mob"]
    chevron = [(By.XPATH, "(//div[@class= 'tcl-homepage-hero__chevron'])[1]/span[@role='button']"), "desk_tab_mob"]

    # model Y screen
    header_model_Y = [(By.XPATH, "(//h1[contains(text() , 'Model Y')])[1]"), "desk_tab_mob"]

    # model 3 desk buttons
    button_order_model_Y_d = [(By.XPATH, "(//div[contains(@class, '__buttons-on-desktop')])[1]/section/a[@title='Custom Order']"), "desk_tab"]

    locators_list = [top_line_offer, top_line_offer_learn_more_link, footer_logo, footer_model_s_link,
                     footer_model_3_link, footer_model_Y_link, footer_model_X_link, footer_model_Y_link, footer_Roof_link,
                     footer_Panels_link, footer_shop_link, footer_account_link, footer_menu_button, header_model_3, para_model_3_d,
                     para_model_3_m, button_demo_model_3_d, button_order_model_3_d, button_demo_model_3_m,
                     button_demo_model_3_m, img, chevron]

    def __init__(self, driver):
        self.driver = driver

    # def save_screenshot(self, test_name):
    #     Common.save_screenshot(self.driver, test_name)

    #  this method will return boolean
    def check_element_is_displayed(self, locator):
        Common.wait_for_element_visibility(locator[0], 2, self.driver)
        is_displayed = Common.is_displayed(Common.get_element(self.driver, locator[0]))
        return is_displayed
