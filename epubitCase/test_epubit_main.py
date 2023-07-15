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

class Test_epubit_main:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize('url, waitTime, type, name', CaseData.epubitCase_data)
    def test_epubit_select_book(self, waitTime, url, type, name):
        driverWait = WebDriverWait(self.driver, waitTime)
        self.driver.get(url)
        self.driver.implicitly_wait(waitTime)
        self.driver.find_element(By.CLASS_NAME, "main_border").click()
        driverWait.until(lambda a:a.find_element(By.CLASS_NAME, "el-input__inner").is_displayed())
        self.driver.find_element(By.CLASS_NAME, "el-input__inner").click()
        self.driver.find_element(By.CLASS_NAME, "el-input__inner").send_keys(name)
        self.driver.find_element(By.CLASS_NAME, "is-plain").click()
        driverWait.until_not(lambda a:a.find_element(By.ID, "el-loading-mask"))
        self.driver.find_element(By.XPATH, "//div[@class='tabs']/span[text()='" + type + "']").click()
        driverWait.until_not(lambda a: a.find_element(By.ID, "el-loading-mask"))
        resultElement = self.driver.find_elements(By.CLASS_NAME, "mode1")
        print("====================验证测试结果====================")
        print("测试数据；type："+type+"\t搜索内容："+name)
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