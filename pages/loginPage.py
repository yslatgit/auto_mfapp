#coding:utf-8
import time
from selenium.webdriver.common.by import By
from pages.basePage import BasePage


class LoginPage(BasePage):
    """登录页面"""
    account_loc = (By.ID,'com.mf.mfhr:id/et_login_phone')
    passwd_loc = (By.ID,'com.mf.mfhr:id/et_login_sms_code')
    submit_loc = (By.ID,'com.mf.mfhr:id/fl_login_submit')
    # assert_loc = (By.XPATH,'//*[@text="我知道了"]')

    def __init__(self,driver):
        BasePage.__init__(self,driver)
        # super().__init__()

    def input_username(self,userName):
        BasePage.logger(u"输入用户名： %s" %userName)
        self.driver.find_element(*self.account_loc).clear()
        self.driver.find_element(*self.account_loc).send_keys(userName)
    def input_passwd(self): #,verificationCode):

        BasePage.logger(u"输入验证码")
        self.driver.find_element(*self.passwd_loc).send_keys("0000")
        # self.driver.find_element(*self.passwd_loc).send_keys(verificationCode)

    def click_submit(self):
        BasePage.logger(u"点击登录按钮")
        self.driver.find_element(*self.submit_loc).click()

    def verify(self,text):
        # com.mf.mfhr:id / main_guide_btn
        assert_loc = (By.XPATH,'//*[@text="%s"]'%text)
        time.sleep(2)
        if self.driver.find_element(*assert_loc):
            BasePage.logger(u"验证是否成功登录：True")
            return True
        else:
            BasePage.logger(u"验证是否成功登录：False")
            return False

    def login(self,username,text):
        self.swipe_block("2","left")
        time.sleep(1)
        self.click_screen()
        self.input_username(username)
        self.input_passwd()
        self.click_submit()
        self.verify(text)