from Config.config import TestData
from Tests.test_base import BaseTest
from WebPages.ViewerLoginPage import ViewerLoginPage
from WebPages.ViewerEnrollCourse import ViewerEnrollCourse
import time

class Test_EnrollCourse(BaseTest):
    def test_home_page_title(self):
        self.ViewerLoginPage = ViewerLoginPage(self.driver)
        home_page = self.ViewerLoginPage.do_login(TestData.VIEWER_EMAIL, TestData.VIEWER_PASSWORD)
        time.sleep(3)
        print("Actual Title:", self.driver.title)
        title = home_page.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_enroll_course(self):
        self.ViewerEnrollCourse = ViewerEnrollCourse(self.driver)
        self.ViewerEnrollCourse.enroll_course()

    def test_view_course(self):
        self.ViewerEnrollCourse = ViewerEnrollCourse(self.driver)
        self.ViewerEnrollCourse.view_course()



