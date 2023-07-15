"""
实现《异步社区》产品搜索功能的自动化测试

图书搜索
搜索Selenium书籍，判断搜索出来的书籍名称是否包含 Selenium

课程搜索
搜索Selenium课程，判断搜索出来的课程是否包含 Selenium

"""
#coding = utf-8

import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from epubitCase.caseData import CaseData
from epubitCase.BaseLayer.executorBase import ExecutorBase
from epubitCase.PageObjects.homePage import HomePage
from epubitCase.PageObjects.bookListPage import BookListPage

class Test_epubit_main():
    def setup_method(self):
        homeUrl = "https://www.epubit.com/"
        self.homePage = HomePage(url= homeUrl)
        #self.bookListPage = BookListPage(self.homePage.get_executor())

    def teardown_method(self):
        self.homePage.quit_executor()
    
    @pytest.mark.parametrize('url, waitTime, type, name', CaseData.epubitCase_data)
    def test_epubit_select_book(self, waitTime, url, type, name):
        self.homePage.get_click_element(self.homePage.selectElement())  # 点击放大镜
        self.homePage.wait_for_element_until(self.homePage.searchResult())      #等待结果页加载
        self.homePage.get_click_element(self.homePage.inputElement())      #点击搜索输入框
        self.homePage.get_send_keys_element(self.homePage.inputElement(), name)     #搜索框输入
        self.homePage.get_click_element(self.homePage.selectProduct())     #点击搜索
        self.homePage.wait_for_element_until_not(self.homePage.filter_loadingMask())   #等待遮罩消失
        self.homePage.get_click_element(self.homePage.changeType(type))  #切换搜索类型
        self.homePage.wait_for_element_until_not(self.homePage.filter_loadingMask())   #等待遮罩消失
        resultElement = self.homePage.selectResult()    #获取所有的搜索结果
        print("====================验证测试结果====================")
        print("测试数据；type："+type+"\t搜索内容："+name)
        bearfruit = False
        if len(resultElement) > 0:
            for book in resultElement:
                bookName = self.homePage.productName(book)
                if name not in bookName:
                    bearfruit = False
                    break
                else:
                    bearfruit = True

        assert bearfruit

    """
    @pytest.mark.parametrize('url, waitTime, type, name', CaseData.epubitCase_data)
    def test_epubit_select(self, waitTime, url, type, name):
        driver = self.homePage.get_executor()
        driverWait = WebDriverWait(driver, waitTime)
        driver.get(url)
        driver.implicitly_wait(waitTime)
        driver.find_element(By.CLASS_NAME, "main_border").click()      #点击放大镜
        driverWait.until(lambda a: a.find_element(By.CLASS_NAME, "el-input__inner").is_displayed())
        driver.find_element(By.CLASS_NAME, "el-input__inner").click()      #点击搜索输入框
        driver.find_element(By.CLASS_NAME, "el-input__inner").send_keys(name)      #搜索框输入
        driver.find_element(By.CLASS_NAME, "is-plain").click()     #点击搜索
        driverWait.until_not(lambda a: a.find_element(By.ID, "el-loading-mask"))
        driver.find_element(By.XPATH, "//div[@class='tabs']/span[text()='" + type + "']").click()  #切换搜索类型
        driverWait.until_not(lambda a: a.find_element(By.ID, "el-loading-mask"))
        resultElement = driver.find_elements(By.CLASS_NAME, "mode1")   #获取所有的搜索结果
        print("====================验证测试结果====================")
        print("测试数据；type：" + type + "\t搜索内容：" + name)
        bearfruit = False
        if len(resultElement) > 0:
            for book in resultElement:
                bookName = book.find_element(By.CLASS_NAME, "list-title").text
                if name not in bookName:
                    bearfruit = False
                    break
                else:
                    bearfruit = True

        assert bearfruit
    """