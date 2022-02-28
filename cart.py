import time
from itertools import product
from selenium.webdriver.chrome import webdriver


def add_to_cart(self,add_to_cart, cheap_products):
    pass


def click_on_cart(driver):
    pass


def price(product, items):
    pass


def cart_page(self, cart):
    # create webdriver instance and navigate to main page
    webdriver.Chrome(executable_path="C:\\Users\\mgirish\\Downloads\\chromedriver.exe")
    driver = webdriver.Chrome()
    driver.maximize_window()
    # navigate to main page
    driver.get("https://weathershopper.pythonanywhere.com/")
    # go to product page depending on the temperature
    time.sleep(3)
    # find the least expensive products
    cheap_products = price(driver)
    # add them to cart
    add_to_cart(driver, cheap_products)
    # go to cart
    click_on_cart(driver)
    time.sleep(3)
    # Verify if the user taken to cart
    if driver.current_url == "https://weathershopper.pythonanywhere.com/cart":
        print("You're in your cart")
    else:
        print('Something went wrong')
        driver.quit()


