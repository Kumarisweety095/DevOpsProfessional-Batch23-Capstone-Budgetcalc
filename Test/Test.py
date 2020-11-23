import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
#driver.implicitly_wait(10)
from selenium.webdriver.chrome.options import Options

option=Options()
option.add_argument("--headless")   
option.add_argument('--no-sandbox')
option.add_argument('start-maximized')
option.add_argument('disable-infobars')
option.add_argument('--disable-extensions')
option.add_argument('--disable-dev-shm-usage')

global driver
options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/google-chrome-stable"
chrome_driver_binary = "/usr/bin/chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, options=option)
    
def test():
    driver.get('http://localhost:80')
    driver.implicitly_wait(10)
    driver.find_element_by_name("amount").click()
    driver.find_element_by_name("amount").clear()
    driver.find_element_by_name("amount").send_keys('1000')
    driver.find_element_by_name("description").click()
    driver.find_element_by_name("description").clear()
    driver.find_element_by_name("description").send_keys("Salary")
    driver.find_element_by_xpath("//button/p").click()
    driver.find_element_by_name("amount").click()
    driver.find_element_by_name("amount").clear()
    driver.find_element_by_name("amount").send_keys("-100")
    driver.find_element_by_name("description").clear()
    driver.find_element_by_name("description").send_keys("Rent")
    driver.find_element_by_xpath("//button/p").click()
    driver.close()
