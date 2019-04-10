#coding:utf-8
from app.Driver import get_driver
from pages.loginPage import LoginPage
from pages.logoutPage import LogoutPage

import unittest

class LogoutCase(unittest.TestCase):
    """退出登录测试"""
    def setUp(self):
        self.driver = get_driver()

    def tearDown(self):
        pass

    def test_logout(self):
        Li = LoginPage(self.driver)
        Li.login("18153529186")
        Lo = LogoutPage(self.driver)
        Lo.logout()