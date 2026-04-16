import time
from selenium.webdriver.common.by import By
from WebPages.BasePage import BasePage
from Config.config import TestData
from WebPages.CreateCoursePage import CreateCoursePage


class CreatorLoginPage(BasePage):

    """By Locater -OR"""

    EMAIL=(By.XPATH, "//input[@placeholder='Enter your email']")
    PASSWORD=(By.XPATH, "//input[@placeholder='Enter your password']")
    SIGNIN_BUTTON=(By.XPATH, "//button[@type='submit']")
    PROFILE=(By.XPATH, "//button[@title='Profile']")
    LOGOUT_BUTTON=(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/header[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]")
    LOGIN_SUCCESS_MSG=(By.XPATH, "(//div[@role='status'])[1]")
    LOGOUT_SUCCESS_MSG=(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]")
    INVALID_LOGIN_MSG=(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]")
    INVALID_EMAIL_MSG=(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]")
    INVALID_PASSWORD_MSG=(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]")
    FORGOT_PASSWORD_LINK=(By.PARTIAL_LINK_TEXT, "Forgot Password?")

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    """Page Actions"""
    """This is used to get the page title"""
    def get_login_page_title(self,title):
        return self.get_title(title)

    """This is used to login to app"""

    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        time.sleep(2)
        self.do_send_keys(self.PASSWORD, password)
        time.sleep(2)
        self.do_click(self.SIGNIN_BUTTON)
        text = self.get_element_text(self.LOGIN_SUCCESS_MSG)
        print(text)
        return CreateCoursePage(self.driver)

    """THis is used to logout from app"""

    def do_logout(self):
        time.sleep(3)
        self.do_click(self.PROFILE)
        self.do_click(self.LOGOUT_BUTTON)
        text = self.get_element_text(self.LOGOUT_SUCCESS_MSG)
        print(text)

    """This is used to login without entering credentials"""

    def default_login(self):
        self.do_click(self.SIGNIN_BUTTON)

    """This is invalid login"""

    def do_invalid_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        time.sleep(2)
        self.do_send_keys(self.PASSWORD, password)
        time.sleep(2)
        self.do_click(self.SIGNIN_BUTTON)
        text = self.get_element_text(self.INVALID_LOGIN_MSG)
        print(text)

    """This is enter invalid email and try to login"""

    def do_invalid_email(self, username, password):
        Email = self.driver.find_element(*self.EMAIL)
        Email.clear()
        self.do_send_keys(self.EMAIL, username)
        time.sleep(2)
        Password = self.driver.find_element(*self.PASSWORD)
        Password.clear()
        self.do_send_keys(self.PASSWORD, password)
        time.sleep(2)
        self.do_click(self.SIGNIN_BUTTON)
        text = self.get_element_text(self.INVALID_EMAIL_MSG)
        print(text)

    """This is enter invalid password and try to login"""

    def do_invalid_password(self, username, password):
        Email = self.driver.find_element(*self.EMAIL)
        Email.clear()
        self.do_send_keys(self.EMAIL, username)
        time.sleep(2)
        Password = self.driver.find_element(*self.PASSWORD)
        Password.clear()
        self.do_send_keys(self.PASSWORD, password)
        time.sleep(2)
        self.do_click(self.SIGNIN_BUTTON)
        text = self.get_element_text(self.INVALID_PASSWORD_MSG)
        print(text)

    """This is to access forgot password page"""

    def forgot_password(self):
        self.do_click(self.FORGOT_PASSWORD_LINK)
        time.sleep(2)
        self.driver.back()


