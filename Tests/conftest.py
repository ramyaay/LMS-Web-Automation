import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Config.config import TestData

@pytest.fixture(scope="class")
def init_driver(request):

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.maximize_window()

    driver.get("http://10.20.161.3:3000/login")

    request.cls.driver = driver

    yield

    driver.quit()