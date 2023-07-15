"""
书籍列表页面元素模块
"""

#coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By

class BookListPage:
    def __init__(self, driver):
        self.driver = driver
    #搜索结果页——搜索类型元素
    def changeType(self, type):
        return self.driver.find_element(By.XPATH, "//div[@class='tabs']/span[text()='" + type + "']")
    #搜索结果页——搜索结果元素
    def selectResult(self):
        return self.driver.find_elements(By.CLASS_NAME, "mode1")
    #搜索结果页——产品名称元素
    def productName(self, resultElement):
        return resultElement.find_element(By.CLASS_NAME, "list-title")