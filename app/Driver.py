#coding:utf-8
from common.tool import read_yaml
from appium import webdriver
import os
import uiautomator2

conf_yaml_path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir)) + r"\testdata\config"
result = read_yaml("conf.yaml", "smartisan", conf_yaml_path)

def get_driver():
    desired_caps = {}
    # print (result)
    desired_caps['platformName'] = result['platformName']
    desired_caps['deviceName'] = result['deviceName']
    desired_caps['platformVersion'] = result['platformVersion']
    desired_caps['appPackage'] = result['appPackage']
    desired_caps['appActivity'] = result['appActivity']
    #要测试的app
    desired_caps['app'] = r"E:\AutoTest-4\app\mfhr_0928_1322.apk"
    #启动app时不要清除app里的原有的数据，自测没用不管true 还是 false 都记录状态
    desired_caps['noReset'] = 'False'
    #使用unicode输入法
    # desired_caps['unicodeKeyboard'] = ['True']
    #重置输入法到初始状态
    # desired_caps['resetKeyboard'] = ['True']
    #捕捉toast
    desired_caps['automationName'] = 'UiAutomator2'
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver


if __name__ == '__main__':
    get_driver()