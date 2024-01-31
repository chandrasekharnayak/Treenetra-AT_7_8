import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope = 'class', autouse=True)
def login_facebook(request):
    #precondition :- setup
    service_object = Service('C:\ChromeDriver\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=service_object)
    driver.get('https://www.facebook.com/')

    yield driver
    #post condtion
    driver.quit()


