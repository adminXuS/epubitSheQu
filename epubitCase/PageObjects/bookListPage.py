"""
书籍列表页面元素模块
"""

#coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from epubitCase.BaseLayer.executorBase import ExecutorBase

class BookListPage(ExecutorBase):
    """
    def __init__(self, driver):
        self.driver = driver
    """
    #搜索结果页——搜索类型元素
    def changeType(self, type):
        return self.get_element("xpath", "//div[@class='tabs']/span[text()='" + type + "']")
        #return self.driver.find_element(By.XPATH, "//div[@class='tabs']/span[text()='" + type + "']")
    #搜索结果页——搜索结果元素
    def selectResult(self):
        return self.get_elements("class", "mode1")
        #return self.driver.find_elements(By.CLASS_NAME, "mode1")
    #搜索结果页——产品名称元素
    def productName(self, resultElement, key, value):
        return self.get_element_in(resultElement, key, value)
        #return resultElement.find_element(By.CLASS_NAME, "list-title")