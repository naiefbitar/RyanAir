from locators import Locators as Locators


class LoginAction:

    def __init__(self, driver):

        self.driver = driver
        self.agree = Locators.agree_xpath
        self.login_xpath = Locators.login_xpath
        self.email = Locators.email_xpath
        self.password = Locators.password_xpath
        self.login_btn = Locators.login_button_xpath

    def agree_btn(self):
        self.driver.find_element_by_xpath(self.agree).click()

    def req_login(self):
        self.driver.find_element_by_xpath(self.login_xpath).click()

    def enter_email(self, email):
        self.driver.find_element_by_xpath(self.email).clear()
        self.driver.find_element_by_xpath(
            self.email).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password).clear()
        self.driver.find_element_by_xpath(
            self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_btn).click()
