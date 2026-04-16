from Config.config import TestData
from Tests.test_base import BaseTest
from WebPages.CreatorLoginPage import CreatorLoginPage
from WebPages.CreateCoursePage import CreateCoursePage
import time

class Test_CreateCouse(BaseTest):
    def test_home_page_title(self):
        self.CreatorLoginPage = CreatorLoginPage(self.driver)
        home_page = self.CreatorLoginPage.do_login(TestData.CREATOR_EMAIL, TestData.CREATOR_PASSWORD)
        time.sleep(3)
        print("Actual Title:", self.driver.title)
        title = home_page.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_create_course(self):
        self.CreateCoursePage=CreateCoursePage(self.driver)
        self.CreateCoursePage.create_course(
            TestData.COURSE_TITLE,
            TestData.COURSE_DESCRIPTION,
            TestData.COURSE_URL,
            TestData.LESSON_TITLE,
            TestData.LESSON_CONTENT,
            TestData.TOPIC_TITLE,
            TestData.TOPIC_CONTENT
        )

    def test_publish_course(self):
        self.CreateCoursePage=CreateCoursePage(self.driver)
        self.CreateCoursePage.publish_course()

    def test_create_course2(self):
        self.CreateCoursePage=CreateCoursePage(self.driver)
        self.CreateCoursePage.create_course2(
            TestData.COURSE_TITLE2,
            TestData.COURSE_DESCRIPTION2,
            TestData.LESSON_TITLE2,
            TestData.LESSON_CONTENT2
        )

    def test_publish_course2(self):
        self.CreateCoursePage=CreateCoursePage(self.driver)
        self.CreateCoursePage.publish_course2()

    def test_create_course3(self):
        self.CreateCoursePage = CreateCoursePage(self.driver)
        self.CreateCoursePage.create_course3(
            TestData.COURSE_TITLE2,
            TestData.COURSE_DESCRIPTION2,
            TestData.LESSON_TITLE2,
            TestData.LESSON_CONTENT2
        )

    def test_course_save_draft(self):
        self.CreateCoursePage = CreateCoursePage(self.driver)
        self.CreateCoursePage.course_save_draft()



