import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from WebPages.BasePage import BasePage


class CreateCoursePage(BasePage):
    """By Locater -OR"""
    CREATE_COURSE_BTN=(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/a[1]")
    COURSE_TITLE=(By.XPATH, "//input[@placeholder='e.g., Advanced JavaScript Masterclass']")
    COURSE_DESCRIPTION=(By.XPATH, "//textarea[@placeholder='Describe what students will learn in this course...']")
    COURSE_URL=(By.XPATH, "//input[@type='url']")
    COURSE_MANDATORY=(By.ID, "mandatoryCourse")
    ADD_LESSON_BTN=(By.XPATH, "//button[normalize-space()='Add Lesson']")
    ADD_LESSON_TITLE=(By.XPATH, "//input[@placeholder='Lesson Title']")
    ADD_LESSON_CONTENT=(By.XPATH, "//div[@class='ql-editor ql-blank']//p")
    TOPIC_CHECKBOX=(By.ID, "hasTopicsCheckbox")
    ADD_TOPIC_BTN=(By.XPATH, "//button[normalize-space()='Add Topic']")
    ADD_TOPIC_TITLE=(By.XPATH, "//input[@placeholder='Topic Title']")
    ADD_TOPIC_CONTENT=(By.XPATH, "//div[@class='bg-white p-4 rounded-xl border-2 border-purple-200 space-y-4']//div[@class='ql-editor ql-blank']")
    SUBMIT_TOPIC_BTN=(By.XPATH, "//button[contains(text(),'✓ Add Topic')]")
    SUBMIT_LESSON_BTN=(By.XPATH, "//button[normalize-space()='Submit Lesson']")
    SUBMIT_COURSE_BTN=(By.XPATH, "//button[contains(text(),'✨ Create Course (1 lesson)')]")
    COURSE_LEVEL_QUIZ_SEL=(By.ID, "quiz-course")
    PUBLISH_COURSE_BTN=(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/button[2]")
    GENERATE_PUBLISH_BTN=(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/button[2]")
    SAVE_AS_DRAFT_BTN=(By.XPATH, "//button[normalize-space()='Save as Draft']")

    """Constructor of the page class"""

    def __init__(self,driver):
        super().__init__(driver)

    """Page Actions"""
    """This is used to get the page title"""

    def get_home_page_title(self, title):
        return self.get_title(title)

    """Create the course generate quiz and publish"""

    def create_course(self, course_title, course_description, course_url, lesson_title, lesson_content, topic_title,
                      topic_content):
        self.do_action_click(self.CREATE_COURSE_BTN)

        self.do_send_keys(self.COURSE_TITLE, course_title)
        self.do_send_keys(self.COURSE_DESCRIPTION, course_description)

        self.scroll_to_element(self.COURSE_URL)
        self.do_send_keys(self.COURSE_URL, course_url)

        self.do_click(self.COURSE_MANDATORY)

        self.do_click(self.ADD_LESSON_BTN)

        self.scroll_to_element(self.ADD_LESSON_TITLE)
        self.do_send_keys(self.ADD_LESSON_TITLE, lesson_title)

        self.scroll_to_element(self.ADD_LESSON_CONTENT)
        self.do_send_keys(self.ADD_LESSON_CONTENT, lesson_content)
        time.sleep(5)

        self.do_action_click(self.TOPIC_CHECKBOX)

        self.do_action_click(self.ADD_TOPIC_BTN)

        self.scroll_to_element(self.ADD_TOPIC_TITLE)
        self.do_send_keys(self.ADD_TOPIC_TITLE, topic_title)

        self.scroll_to_element(self.ADD_TOPIC_CONTENT)
        self.do_send_keys(self.ADD_TOPIC_CONTENT, topic_content)

        self.do_action_click(self.SUBMIT_TOPIC_BTN)

        self.do_click(self.SUBMIT_LESSON_BTN)

        self.scroll_to_element(self.SUBMIT_COURSE_BTN)
        self.do_click(self.SUBMIT_COURSE_BTN)

    def publish_course(self):
        self.do_click(self.COURSE_LEVEL_QUIZ_SEL)
        self.do_click(self.GENERATE_PUBLISH_BTN)
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.accept()
        time.sleep(30)

    """Create the course without generating quiz"""

    def create_course2(self, course_title, course_description, lesson_title, lesson_content):
        self.do_action_click(self.CREATE_COURSE_BTN)

        self.do_send_keys(self.COURSE_TITLE, course_title)
        self.do_send_keys(self.COURSE_DESCRIPTION, course_description)

        self.do_action_click(self.ADD_LESSON_BTN)

        self.do_send_keys(self.ADD_LESSON_TITLE, lesson_title)

        self.do_send_keys(self.ADD_LESSON_CONTENT, lesson_content)
        time.sleep(2)

        self.do_action_click(self.SUBMIT_LESSON_BTN)

        self.scroll_to_element(self.SUBMIT_COURSE_BTN)
        self.do_click(self.SUBMIT_COURSE_BTN)

    def publish_course2(self):
        self.do_click(self.PUBLISH_COURSE_BTN)
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.accept()
        time.sleep(3)

    """Create the course saved and saved in the draft"""

    def create_course3(self, course_title, course_description, lesson_title, lesson_content):
        time.sleep(3)
        self.do_action_click(self.CREATE_COURSE_BTN)

        self.do_send_keys(self.COURSE_TITLE, course_title)
        self.do_send_keys(self.COURSE_DESCRIPTION, course_description)

        self.do_action_click(self.ADD_LESSON_BTN)

        self.do_send_keys(self.ADD_LESSON_TITLE, lesson_title)

        self.do_send_keys(self.ADD_LESSON_CONTENT, lesson_content)
        time.sleep(2)

        self.do_action_click(self.SUBMIT_LESSON_BTN)

        self.scroll_to_element(self.SUBMIT_COURSE_BTN)
        self.do_click(self.SUBMIT_COURSE_BTN)

    def course_save_draft(self):
        self.do_click(self.SAVE_AS_DRAFT_BTN)







    









