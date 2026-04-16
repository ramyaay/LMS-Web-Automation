import time
import pytest
from Config.config import TestData
from WebPages.CreatorLoginPage import CreatorLoginPage
from Tests.test_base import BaseTest
from WebPages.DraftCourse import DraftCourse

class Test_DraftCourse(BaseTest):

    def test_home_page_title(self):
        self.CreatorLoginPage = CreatorLoginPage(self.driver)
        home_page = self.CreatorLoginPage.do_login(TestData.CREATOR_EMAIL, TestData.CREATOR_PASSWORD)
        time.sleep(3)
        print("Actual Title:", self.driver.title)
        title = home_page.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_draft_course_cancel(self):
        self.DraftCourse = DraftCourse(self.driver)
        self.DraftCourse.draft_course_cancel()

    def test_draft_course_edit_save(self):
        self.DraftCourse = DraftCourse(self.driver)
        self.DraftCourse.draft_course_edit_save(TestData.DRAFT_COURSE_TITLE)

    def test_delete_draft_course(self):
        self.DraftCourse = DraftCourse(self.driver)
        self.DraftCourse.delete_draft_course()

    def test_update_draft_course(self):
        self.DraftCourse = DraftCourse(self.driver)
        self.DraftCourse.update_draft_course()