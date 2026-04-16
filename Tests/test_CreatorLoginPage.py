import time
import pytest
from Config.config import TestData
from WebPages.CreatorLoginPage import CreatorLoginPage
from Tests.test_base import BaseTest

class Test_Login(BaseTest):

    def test_login_page_title(self):
        self.CreatorLoginPage=CreatorLoginPage(self.driver)
        title = self.CreatorLoginPage.get_title("LMS Onboarding System")
        assert "LMS Onboarding System" in title

    def test_login(self):
        self.CreatorLoginPage=CreatorLoginPage(self.driver)
        time.sleep(3)
        self.CreatorLoginPage.do_login(TestData.CREATOR_EMAIL,TestData.CREATOR_PASSWORD)
        time.sleep(3)

    def test_logout(self):
        self.CreatorLoginPage=CreatorLoginPage(self.driver)
        self.CreatorLoginPage.do_logout()

    def test_default_login(self):
        self.CreatorLoginPage=CreatorLoginPage(self.driver)
        self.CreatorLoginPage.do_click(self.CreatorLoginPage.SIGNIN_BUTTON)
        assert False

    def test_invalid_login(self):
        self.CreatorLoginPage=CreatorLoginPage(self.driver)
        self.CreatorLoginPage.do_login(TestData.INVALID_EMAIL, TestData.INVALID_PASSWORD)
        assert False

    def test_invalid_email(self):
        self.CreatorLoginPage=CreatorLoginPage(self.driver)
        self.CreatorLoginPage.do_invalid_email(TestData.INVALID_EMAIL,TestData.CREATOR_PASSWORD)
        assert False

    def test_invalid_password(self):
        self.CreatorLoginPage=CreatorLoginPage(self.driver)
        self.CreatorLoginPage.do_invalid_password(TestData.CREATOR_EMAIL,TestData.INVALID_PASSWORD)
        assert False

    def test_forgot_password(self):
        self.CreatorLoginPage=CreatorLoginPage(self.driver)
        self.CreatorLoginPage.forgot_password()

