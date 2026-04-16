from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

"""This class is the parent of all pages"""
"""It contains all the generic methods and utilities for all the pages"""

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_contains(title))
        return self.driver.title

    def do_send_keys(self, by_locater, text):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(by_locater)).send_keys(text)

    def get_element_text(self,by_locater):
        element=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locater))
        return element.text

    def do_click(self, locator):
        element = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))
        element.click()

    def is_visible(self, by_locater):
        element=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locater))
        return element.is_displayed()

    def alert_text(self):
        alert=self.driver.switch_to.alert
        return alert.text

    def select_dropdown_value(self, dropdown_locator, options_locator, data_value):
        self.do_click(dropdown_locator)
        options = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(options_locator))
        for option in options:
            if option.text.strip() == data_value:
                option.click()
                return True

        raise Exception(f"Value '{data_value}' not found in dropdown")

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def scroll_to_element(self, locator):
        element = self.get_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def do_action_click(self, locator):
        element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator))

        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)

        actions = ActionChains(self.driver)
        actions.move_to_element(element).pause(1).click().perform()

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")