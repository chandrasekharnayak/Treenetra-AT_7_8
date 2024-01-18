from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

service_object = Service('C:\ChromeDriver\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

'''def action_chain():
    hover_element = driver.find_element(By.ID,'mousehover') # seraching hover elemeent
    action = ActionChains(driver)
    return action.move_to_element(hover_element).perform()'''

#top
# action_chain()
# top_click = driver.find_element(By.XPATH,"//a[text()='Top']")
# time.sleep(2)
# top_click.click()

#reload
'''action_chain()
reload_click = driver.find_element(By.XPATH,"//a[text()='Reload']")
time.sleep(2)
reload_click.click()'''


#double_click
element_to_double_click  = driver.find_element(By.ID,"opentab")
action = ActionChains(driver)
action.double_click(element_to_double_click).perform()

time.sleep(3)
driver.quit()
