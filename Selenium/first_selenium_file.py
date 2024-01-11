from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service_object = Service('C:\ChromeDriver\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

driver.get('https://www.naukri.com/')#opening url/heat url

time.sleep(5)

driver.quit() # single web application
driver.close() #multile web application

'''what is locator 
selenium have 8 types of locator

ID,NAME,CLASSNAME,TAGNAME,LINKTEXT,PARTIALLINKTEXT,XAPTH,CSSSELECTOR'''

#1. open a website or web application through selenium
#2. then connection the web element
#3. test the required fields