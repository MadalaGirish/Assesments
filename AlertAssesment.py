import time
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains


ser=Service("C:\\Users\\mgirish\\Downloads\\chromedriver.exe")
driver=webdriver.Chrome(service=ser)
driver.get("https://the-internet.herokuapp.com/")
driver.find_element(By.XPATH, "//*[@id='content']/ul/li[29]/a").click()
driver.maximize_window()
btn=driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[3]/button")
btn.click()
alert_1=Alert(driver)
alert_1.send_keys("Ex- Test")
alert_1.accept()
time.sleep(4)
driver.quit()

