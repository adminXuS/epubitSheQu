"""
首页元素模块
"""

#coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from epubitCase.BaseLayer.executorBase import ExecutorBase

class HomePage(ExecutorBase):
    """
    def __init__(self, driver):
        self.driver = driver
    #请求函数
    def requestsGet(self, url):
        return self.driver.get(url)
    """
    #首页——放大镜元素
    def selectElement(self):
        return self.get_element("class", "main_border")
        #return self.driver.find_element(By.CLASS_NAME, "main_border")
    #搜索页——搜索框元素
    def inputElement(self):
        return self.get_element("class", "el-input__inner")
        #return self.driver.find_element(By.CLASS_NAME, "el-input__inner")
    #搜索页——搜索产品元素
    def selectProduct(self):
        return self.get_element("class", "is-plain")
        #return self.driver.find_element(By.CLASS_NAME, "is-plain")
