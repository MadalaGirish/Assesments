import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="C:\\Users\\mgirish\\Downloads\\chromedriver.exe")
driver.get("https://www.goibibo.com/flights/")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='get_sign_in']/p").click()
driver.find_element_by_name("phone").send_keys("8093220267")
#driver.find_element_by_css_selector("input.loginCont__btn").click()


#Goibibo Logo
driver.get("https://www.goibibo.com/flights/")
#Goibibo_logo_By_xpath(//a[@class=gi-header-logo__home])

#Login and Sign Up
driver.find_element_by_xpath("//*[@id='get_sign_in']/p").click()

#Hotels, Flights
driver.find_element_by_css_selector("a.nav-link active").click()

#From
driver.find_element_by_link_text("Enter city or airport").click()

#Search
driver.find_element_by_css_selector("span.sc-dFtzxp hwZghA")

#Student Fare
driver.find_element_by_css_selector("li.sc-bdvvtL goIptw")

#Products
driver.find_element_by_css_selector("li.sc-cZMNgc dCkKyZ")

#product
relative= "//*[@class='fb button orange padLR30 txtTransUpper marginB10 fltHpySrchBtn']"


