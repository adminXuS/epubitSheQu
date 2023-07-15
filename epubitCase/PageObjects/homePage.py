"""
首页元素模块
"""

#coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
    #请求函数
    def requestsGet(self, url):
        return self.driver.get(url)
    #首页——放大镜元素
    def selectElement(self):
        return self.driver.find_element(By.CLASS_NAME, "main_border")
    #搜索页——搜索框元素
    def inputElement(self):
        return self.driver.find_element(By.CLASS_NAME, "el-input__inner")
    #搜索页——搜索产品元素
    def selectProduct(self):
        return self.driver.find_element(By.CLASS_NAME, "is-plain")
