#coding:utf-8

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.tool import *
import time
import logging

yaml_path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir)) + r"\testdata\config"

class BasePage(object):
    """所有page的基类"""
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,*loc):
        """重写查找单个元素的方法"""
        try:
            WebDriverWait(self.driver,30).until(lambda x:x.find_element(*loc))
            return self.driver.find_element(*loc)
        except Exception:
            print(u"%s未找到%s元素")%(loc)

    def find_elements(self,*loc):
        """重写查找多个元素的方法"""
        try:
            WebDriverWait(self.driver,30).until(lambda x:x.find_element(*loc))
            return self.driver.find_element(*loc)
        except Exception:
            print(u"%s未找到%s元素")%(loc)


    def swipe_block(self,times,direction):
        time.sleep(2)
        """滑动手机页面:滑动次数--time滑动方向--direction"""
        #{'height': 2560, 'width': 1440}
        x = int(self.driver.get_window_size()['width'])
        # print (x)
        y = int(self.driver.get_window_size()['height'])
        self.logger(u"手机的屏幕尺寸为{width:%d，heigkt:%d}" %(x,y))
        # self.logger(u"滑动的次数为%d次，方向是%s")%(time,direction)
        times = int(times)
        for i in range(times):
            if direction == "left":
                self.driver.swipe(x * 0.9, y * 0.5, x * 0.1, y * 0.5, 1000)
            elif direction == "right":
                self.driver.swipe(x * 0.1, y * 0.5, x * 0.9, y * 0.5, 1000)

    @classmethod
    def logger(self,something,f ="f"):
        """自定义log函数"""
        logger_path = read_yaml("conf.yaml","logpath",yaml_path)
        # print (logger_path)
        #声明一个log
        mylogger = logging.getLogger('AutoTest')
        #设置log等级
        mylogger.setLevel(logging.DEBUG)
        #判断是输出到文件还是控制台，默认为文件
        if f == "fh":
            #创建一个handler写入文件
            rq = time.strftime('%Y-%m%d-%H%M', time.localtime(time.time()))
            logger_path = logger_path + "%s.log"%rq
            fh = logging.FileHandler(logger_path)
            #定义handler输出格式
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            mylogger.addHandler(fh)
            mylogger.info(something)
            mylogger.removeHandler(fh)
        else:
            # 创建一个handler输出控制台
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch = logging.StreamHandler()
            ch.setFormatter(formatter)
            mylogger.addHandler(ch)
            mylogger.info(something)
            mylogger.removeHandler(ch)




    def click_screen(self,x=1000,y=1000):
        """点击屏幕（1000,1000）位置"""
        os.system("adb shell input tap %d %d" %(x,y))

    def find_toast(self, message):
        '''判断toast信息'''
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, message)))
            return True
        except:
            return False





if __name__ == '__main__':
    b = BasePage("1")
    b.logger(u"你好")