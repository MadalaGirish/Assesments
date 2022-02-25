import  time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

ser=Service("C:\\Users\\mgirish\\Downloads\\chromedriver.exe")
driver=webdriver.Chrome(service=ser)
driver.maximize_window()
driver.get("https://webdriveruniversity.com/")
driver.implicitly_wait(5)

#1.ButtonClick
#driver.find_element_by_xpath("//*[@id='button-clicks']/div/div[1]/h1").click()

#dropdown
# driver.find_element(By.XPATH, "//h1[text()='DROPDOWN, CHECKBOXE(S) & RADIO BUTTON(S)']").click()
# driver.switch_to.window(driver.window_handles[1])
# select = Select(driver.find_element(By.XPATH, "//select[@id='dropdowm-menu-1']"))
# select.select_by_index('2')
# driver.find_element(By.XPATH, "//input[@value='option-1']").click()
# driver.find_element(By.XPATH, "//input[@value='green']").click()
# driver.find_element(By.XPATH, "//input[@value='lettuce']").click()
# select1 = Select(driver.find_element(By.ID, 'fruit-selects'))
# select1.select_by_index('2')

#textfield
# driver.find_element(By.XPATH, "//h1[text()='AUTOCOMPLETE TEXTFIELD']").click()
# driver.switch_to.window(driver.window_handles[1])
# driver.find_element(By.ID, 'myInput').send_keys("Girish")
# time.sleep(3)
# driver.find_element(By.ID, 'submit-button').click()

#Scrolling
# driver.find_element_by_xpath("//*[@id='scrolling-around']/div/div[1]/h1").click()
# scroling=driver.find_element_by_id("zone1")
# entiti=driver.find_element_by_id("zone2-entries")
# Ent=driver.find_element_by_id("zone3-entries")
# actions=ActionChains(driver)
# actions.move_to_element(scroling)

#To do list
# driver.find_element(By.XPATH, "//h1[text()='TO DO LIST']").click()
# driver.switch_to.window(driver.window_handles[1])
# driver.find_element(By.XPATH, "//input[@placeholder='Add new todo']").send_keys("Test")
# driver.find_element(By.XPATH, "//input[@placeholder='Add new todo']").send_keys(Keys.ENTER)
# driver.find_element(By.XPATH, '//*[@id="container"]/ul/li[4]').click()
# driver.find_element(By.XPATH, '//*[@id="container"]/ul/li[4]/span/i').click()

#File Upload
# driver.find_element_by_xpath("//*[@id='file-upload']/div/div[1]/h1").click()
# driver.switch_to.window(driver.window_handles[1])
# driver.find_element(By.ID, 'myFile').send_keys("C://Users/mgirish/Picture/Screenshots")
# driver.find_element(By.ID, 'submit-button').click()

#Test-action
driver.find_element(By.XPATH, "//h1[text()='ACTIONS']").click()
driver.switch_to.window(driver.window_handles[1])
actionChains = ActionChains(driver)
source_element = driver.find_element(By.ID, 'Action')
dest_element = driver.find_element(By.ID, 'Action')
actionChains.drag_and_drop(source_element, dest_element).perform()
color = driver.find_element(By.ID, 'double-click')
actionChains.double_click(color).perform()
first_hover = driver.find_element(By.XPATH, "//button[text()= 'Hover Over Me First!']")
actionChains.move_to_element(first_hover).perform()
second_hover = driver.find_element(By.XPATH, "//button[text()= 'Hover Over Me Second!']")
actionChains.move_to_element(second_hover).perform()
third_hover = driver.find_element(By.XPATH, "//button[text()= 'Hover Over Me Third!']")
actionChains.move_to_element(third_hover).perform()
click = driver.find_element(By.ID, 'click-box')
actionChains.click_and_hold(on_element=click).perform()
double = click.text
print(double)
assert double == 'print'