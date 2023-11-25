from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service_object = Service('C:\ChromeDriver\chromedriver-win32\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

driver.get('https://www.amazon.in/')

try:
    books_dropdown = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.ID,"searchDropdownBox"))
    )
    books_dropdown.click()

    books_option = WebDriverWait(driver,5).until(
        EC.element_to_be_clickable((By.XPATH,"//option[text()='Books']"))
    )
    books_option.click()

    search_box = WebDriverWait(driver,5).until(
        EC.element_to_be_clickable((By.ID,"twotabsearchtextbox"))
    )
    search_box.send_keys("AWS")
    search_box.submit


finally:
    time.sleep(3)
    driver.quit()





