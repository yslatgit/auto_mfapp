#coding:utf-8
from app.Driver import get_driver
from pages.loginPage import LoginPage
from common.tool import *
import unittest

yaml_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..')) + r"\testdata\casedata"

class LoginCase(unittest.TestCase):
    """登录测试页面"""
    data = read_yaml("login.yaml", "account", yaml_path)
    asserts = read_yaml("login.yaml", "assert", yaml_path)
    # print(type(data[0]))
    # print(asserts[0])
    def setUp(self):
        # os.system("adb start-server")
        self.driver = get_driver()
        # self.Lo = LoginPage(self.driver)
        pass
    def tearDown(self):
        # self.driver.quit()
        pass
    def test_login_a(self):
        Lo = LoginPage(self.driver)
        Lo.login(self.data[0],self.asserts[0])

        # Lo.swipe_block("2", "left")
        # time.sleep(1)
        # Lo.click_screen()
        # Lo.input_username("18153529186")
        # Lo.input_passwd()
        # Lo.click_submit()

    def test_login_b(self):
        # time.sleep(2)
        Lo = LoginPage(self.driver)
        Lo.login(self.data[1],self.asserts[0])

def main():
    unittest.main()

if __name__ == '__main__':
    main()