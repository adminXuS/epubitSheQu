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
from epubitCase.PageObjects.homePage import HomePage
from epubitCase.PageObjects.searchListPage import SearchListPage
from epubitCase.PageObjects.searchPage import SearchPage
from config import Config

class Test_epubit_main():
    def setup_method(self):
        homeUrl = Config.url
        self.homePage = HomePage(url= homeUrl)      #首页实例
        self.searchListPage  = SearchListPage(executor = self.homePage.get_executor())      #搜索结果列表页实例
        self.searchPage = SearchPage(executor= self.homePage.get_executor())        #搜索页实例

    def teardown_method(self):
        self.homePage.quit_executor()
    #解耦测试用例和操作
    @pytest.mark.parametrize('waitTime, type, name', CaseData.epubitCase_data)
    def test_epubit_select_book(self, waitTime, type, name):
        self.homePage.get_click_element(self.homePage.selectElement())  # 点击放大镜
        self.homePage.wait_for_element_until(self.searchPage.searchResult(), seconds= waitTime)      #等待结果页加载
        self.homePage.get_click_element(self.searchPage.inputElement())      #点击搜索输入框
        self.homePage.get_send_keys_element(self.searchPage.inputElement(), name)     #搜索框输入
        self.homePage.get_click_element(self.searchPage.selectProduct())     #点击搜索
        self.homePage.wait_for_element_until_not(self.searchListPage.filter_loadingMask(), seconds= waitTime)   #等待遮罩消失
        self.homePage.get_click_element(self.searchListPage.changeType(type))  #切换搜索类型
        self.homePage.wait_for_element_until_not(self.searchListPage.filter_loadingMask(), seconds= waitTime)   #等待遮罩消失
        resultElement = self.searchListPage.selectResult()    #获取所有的搜索结果
        print("====================验证测试结果====================")
        print("测试数据；type："+type+"\t搜索内容："+name)
        bearfruit = False
        if len(resultElement) > 0:
            for book in resultElement:
                bookName = self.searchListPage.productName(book)
                if name not in bookName:
                    bearfruit = False
                    break
                else:
                    bearfruit = True

        assert bearfruit

    @pytest.mark.parametrize('waitTime, type, name', CaseData.epubitCase_data1)
    def test_epubit_select(self, waitTime, type, name):
        driver = self.homePage.get_executor()
        driverWait = WebDriverWait(driver, waitTime)
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
