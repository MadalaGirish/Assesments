import time
import unittest

import home as home
from selenium import webdriver
from config.config import TestData
from Pages.Appliances import Appliances
from Pages.Base import Base
from Pages.Fashion import Fashion
from Pages.Home_Link import Home_Link
from Pages.Home_Page import Home_Page
from Pages.Login import Login


class cart_item_verify(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.driver = None


    def test_add_items_and_verify(self):
        login = Login(self.driver)
        home = Home_Page(self.driver)
        fashion = Fashion(self.driver)
        home_link = Home_Link(self.driver)
        appliances = Appliances(self.driver)
        base = Base(self.driver)
        login.login_into_app()
        time.sleep(4)
        home.hover_fashion_and_select_element()
        fashion.select_fashion_product_and_add_to_cart()
        home.back_to_old_window()
        base.backward()
        time.sleep(4)
        home.hover_appliances_and_select_element()
        appliances.select_appliances_product_and_add_to_cart()
        home.back_to_old_window()
        base.backward()
        home.hover_home_and_select_element()
        home_link.select_kitchen_product_and_add_to_cart()
