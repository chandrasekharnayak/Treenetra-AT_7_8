from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

@pytest.mark.usefixtures('login_facebook')
class TestFacebook():
        def test_facebook_login(self,login_facebook):
                user_name = login_facebook.find_element(By.ID, 'email').send_keys('debiprasad789@gmail.com')
                password = login_facebook.find_element(By.ID, 'pass').send_keys('BaNty@8787')
                submit = login_facebook.find_element(By.NAME, 'login').click()
                print('Sucefull Login')
                time.sleep(5)

        @pytest.mark.skip('Want to skip')
        def test_facebook_search(self,login_facebook):
                login_facebook.find_element(By.XPATH, "//input[@dir='ltr']").send_keys('debiprasad')
                print('Search box is working')
                time.sleep(3)
        def test_facebook_options_working_or_not(self,login_facebook):
                login_facebook.find_element(By.XPATH,"//span[contains(text(),'Friends')]").click()
                print('Clickable')

