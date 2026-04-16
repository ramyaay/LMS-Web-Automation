import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from WebPages.BasePage import BasePage
from Config.config import TestData

class DraftCourse(BasePage):
    SEL_DRAFT_COURSE=(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/a[1]/div[1]")
    SAVE_AND_EXIT_BTN=(By.XPATH, "//button[normalize-space()='Save & Exit']")
    UPDATE_COURSE_BTN=(By.XPATH, "//button[normalize-space()='Update Course']")
    DELETE_COURSE_BTN=(By.XPATH, "//button[normalize-space()='Delete Course']")
    CANCEL_BTN=(By.XPATH, "//button[normalize-space()='Cancel']")
    COURSE_TITLE=(By.XPATH, "//input[@placeholder='e.g., Advanced JavaScript Masterclass']")
    UPDATE_PUBLISH_BTN=(By.XPATH, "//button[contains(text(),'📤 Publish Course')]")


    def __init__(self,driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def draft_course_cancel(self):
        self.do_click(self.SEL_DRAFT_COURSE)
        self.do_action_click(self.CANCEL_BTN)

    def delete_draft_course(self):
        self.scroll_to_top()
        self.do_click(self.SEL_DRAFT_COURSE)
        self.do_action_click(self.DELETE_COURSE_BTN)
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.accept()

    def update_draft_course(self):
        self.scroll_to_top()
        self.do_click(self.SEL_DRAFT_COURSE)
        self.do_action_click(self.UPDATE_COURSE_BTN)
        self.do_click(self.UPDATE_PUBLISH_BTN)
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.accept()

    def draft_course_edit_save(self, title):
        self.scroll_to_top()
        self.do_click(self.SEL_DRAFT_COURSE)
        Title=self.driver.find_element(*self.COURSE_TITLE)
        Title.clear()
        self.do_send_keys(self.COURSE_TITLE, title)
        self.do_action_click(self.SAVE_AND_EXIT_BTN)


