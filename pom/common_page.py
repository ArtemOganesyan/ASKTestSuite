from pom.home_page import HomePage
from pom.sign_in_page import SignInPage

# this class allows for accessing of all pages classes using single instance
class CommonPage:
    def __init__(self, driver):
        self.sign_in_page = SignInPage(driver)
        self.homepage = HomePage(driver)
