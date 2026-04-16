from WebPages.BasePage import BasePage
import time
from selenium.webdriver.common.by import By

class ViewerEnrollCourse(BasePage):
    """By Locater -OR"""
    EXPLORE_COURSE_BTN=(By.XPATH, "//button[normalize-space()='Explore Courses']")
    ENROLL_BTN=(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]")
    BACK_TO_MY_COURSE_BTN=(By.XPATH, "//button[normalize-space()='Back To My Courses']")
    SELECT_COURSE_TO_START=(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/a[2]/div[1]")
    START_LEARNING_BTN=(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/button[1]")
    MARK_CONTENT_AS_COMPLETED=(By.XPATH, "//button[normalize-space()='Mark Content as Completed']")
    TOPIC1_VIEW_BTN=(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/button[1]/div[1]/span[2]")
    TOPIC1_COMPLETE_BTN=(By.XPATH, "//button[normalize-space()='Mark Content as Completed']")
    NEXT_TOPIC_BTN=(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/button[1]")
    TOPIC2_VIEW_BTN=(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/button[2]/div[1]/span[2]")
    TOPIC2_COMPLETE_BTN=(By.XPATH, "//button[normalize-space()='Mark Content as Completed']")
    GO_TO_FINAL_QUIZ_BTN=(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/button[2]")
    START_FINAL_ASSESSMENT_BTN=(By.XPATH, "//button[normalize-space()='Start Final Assessment']")
    TAKE_QUIZ_BTN=(By.XPATH, "//button[@title='Take Lesson Quiz']")

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)

    """This is used to enroll the course"""

    def enroll_course(self):
        self.do_click(self.EXPLORE_COURSE_BTN)
        self.do_click(self.ENROLL_BTN)
        self.do_click(self.BACK_TO_MY_COURSE_BTN)

    """This is used to view and complete the course"""

    def view_course(self):
        self.do_click(self.SELECT_COURSE_TO_START)
        self.do_click(self.START_LEARNING_BTN)
        self.do_click(self.MARK_CONTENT_AS_COMPLETED)
        self.do_click(self.TOPIC1_VIEW_BTN)
        self.do_click(self.TOPIC1_COMPLETE_BTN)
        self.do_click(self.NEXT_TOPIC_BTN)
        self.do_click(self.TOPIC2_VIEW_BTN)
        self.do_click(self.TOPIC2_COMPLETE_BTN)
        self.do_click(self.GO_TO_FINAL_QUIZ_BTN)
        self.do_click(self.START_FINAL_ASSESSMENT_BTN)
        self.do_click(self.TAKE_QUIZ_BTN)




