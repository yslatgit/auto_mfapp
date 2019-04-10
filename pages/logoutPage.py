#coding:utf-8
import time
from selenium.webdriver.common.by import By
from pages.basePage import BasePage

class LogoutPage(BasePage):
    """退出登录页面"""
    main_user_loc = (By.ID,'com.mf.mfhr:id/iv_main_user')
    setting_loc = (By.ID,'com.mf.mfhr:id/llSetting')
    logout_loc = (By.ID,'com.mf.mfhr:id/tv_settings_logout')
    i_know_loc = (By.ID,'com.mf.mfhr:id/main_guide_btn')
    def __init__(self,driver):
        BasePage.__init__(self,driver)

    def click_my(self):
        # self.driver.click_screen(x=800, y=2000)\
        self.driver.find_element(*self.i_know_loc).click()
        self.driver.find_element(*self.main_user_loc).click()

    def click_setting(self):
        self.driver.find_element(*self.setting_loc).click()

    def logout(self):
        self.click_my()
        self.click_setting()
        self.driver.find_element(*self.setting_loc).click()
        print(self.find_toast("退出登录成功"))