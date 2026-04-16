import time
import pytest
from Config.config import TestData
from WebPages.ViewerLoginPage import ViewerLoginPage
from Tests.test_base import BaseTest

class Test_Login(BaseTest):

    def test_login_page_title(self):
        self.ViewerLoginPage=ViewerLoginPage(self.driver)
        title = self.ViewerLoginPage.get_title("LMS Onboarding System")
        assert "LMS Onboarding System" in title

    def test_login(self):
        self.ViewerLoginPage=ViewerLoginPage(self.driver)
        time.sleep(3)
        self.ViewerLoginPage.do_login(TestData.VIEWER_EMAIL,TestData.VIEWER_PASSWORD)
        time.sleep(3)

    def test_logout(self):
        self.ViewerLoginPage=ViewerLoginPage(self.driver)
        self.ViewerLoginPage.do_logout()

    def test_default_login(self):
        self.ViewerLoginPage=ViewerLoginPage(self.driver)
        self.ViewerLoginPage.do_click(self.ViewerLoginPage.SIGNIN_BUTTON)
        assert False

    def test_invalid_login(self):
        self.ViewerLoginPage=ViewerLoginPage(self.driver)
        self.ViewerLoginPage.do_login(TestData.INVALID_EMAIL, TestData.INVALID_PASSWORD)
        assert False

    def test_invalid_email(self):
        self.ViewerLoginPage=ViewerLoginPage(self.driver)
        self.ViewerLoginPage.do_invalid_email(TestData.INVALID_EMAIL,TestData.VIEWER_PASSWORD)
        assert False

    def test_invalid_password(self):
        self.ViewerLoginPage=ViewerLoginPage(self.driver)
        self.ViewerLoginPage.do_invalid_password(TestData.VIEWER_EMAIL,TestData.INVALID_PASSWORD)
        assert False

    def test_forgot_password(self):
        self.ViewerLoginPage=ViewerLoginPage(self.driver)
        self.ViewerLoginPage.forgot_password()

