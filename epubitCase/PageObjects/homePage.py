"""
首页元素模块
"""

#coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from epubitCase.BaseLayer.executorBase import ExecutorBase
from epubitCase.PageObjects.bookListPage import BookListPage

class HomePage(BookListPage):
    """
    BookListPage 模块继承 ExecutorBase模块
    继承 BookListPage 时同时页继承 ExecutorBase 模块，
    ExecutorBase 模块初始化了 浏览器驱动和get请求
    不需要浏览器驱动初始化函数和请求函数
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
    #等待搜索结果出现
    def searchResult(self):
        return self.get_element("class", "el-input__inner")