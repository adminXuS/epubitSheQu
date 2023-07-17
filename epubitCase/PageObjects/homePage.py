"""
首页元素模块
"""

#coding = utf-8

from epubitCase.PageObjects.siteHeader import SiteHeader

class HomePage(SiteHeader):
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
    pass