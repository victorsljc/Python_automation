import time

url='https://selectorshub.com/xpath-practice-page/'
from selenium import  webdriver
from pom_project.locators import *
driver = webdriver.Chrome()
driver.get(url)

def test_browser_navigation():
    driver.refresh()
    time.sleep(10)
    driver.maximize_window()
    driver.find_element(By.XPATH,menu_help).click()
    time.sleep(5)
    driver.minimize_window()
    driver.back()
    time.sleep(5)
    driver.maximize_window()
    driver.forward()
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
    driver.back()
    time.sleep(5)



