import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(autouse=True)#function,class,session,module
def login_and_logout_facebook(request):
    #Precondition
    service_object = Service('C:\ChromeDriver\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=service_object)

    driver.get('https://www.facebook.com/')

    user_name = driver.find_element(By.ID,'email').send_keys('debiprasad789@gmail.com')
    password = driver.find_element(By.ID,'pass').send_keys('BaNty@143')
    submit = driver.find_element(By.NAME,'login').click()
    time.sleep(5)

    yield driver
    #postcondition :- teardown
    #write logout functionality of facebook

