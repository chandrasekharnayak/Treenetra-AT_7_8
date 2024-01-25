import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_check_facebook_text_field(login_and_logout_facebook):

    login_and_logout_facebook.find_element(By.XPATH,"//input[@dir='ltr']").send_keys('debiprasad')
    time.sleep(3)