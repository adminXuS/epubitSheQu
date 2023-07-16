"""
测试案例
筛选电子书功能
1、首页——电子书
2、图书——>软件开发——>软件工程与方法——>软件测试与质量控制
3、点击 第一个结果 查看详情
4、验证 分类是否为：软件测试与质量控制

筛选课程功能
1、首页——课程
2、图书——>软件开发——>软件工程与方法——>软件测试与质量控制
3、点击 第一个结果 查看详情
4、验证 分类是否为：软件测试与质量控制
"""
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from epubitCase.caseData import CaseData

class Test_epubit_filter:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize("url, waitTime, text, title", CaseData.filter_data)
    def test_book_filter(self, url, waitTime, text, title):
        driverWait = WebDriverWait(self.driver, waitTime)
        driverActionChains = ActionChains(self.driver)
        self.driver.get(url)
        driverWait.until(lambda a: a.find_element(By.CLASS_NAME, "tabbar-link").is_displayed())
        self.driver.find_element(By.XPATH, "//div[@class='header-item']/span[text()='"+text+"']").click()
        driverWait.until(lambda a: a.find_element(By.ID, "pagesBottom").is_displayed())
        for i in range(1, 4):
            driverActionChains.move_to_element(
                self.driver.find_element(By.XPATH, "(//div[@class='select-box_item--title'])["+str(i)+"]")).perform()
            driverActionChains.click(self.driver.find_element(By.XPATH, "//span[@title='"+title[i - 1]+"']")).perform()
            time.sleep(1)
        #driverActionChains.move_to_element(
            #self.driver.find_element(By.XPATH, "(//div[@class='select-box_item--title'])[2]")).perform()
        #driverActionChains.click(self.driver.find_element(By.XPATH, "//span[@title='软件工程与方法']")).perform()
        #driverActionChains.move_to_element(
            #self.driver.find_element(By.XPATH, "(//div[@class='select-box_item--title'])[3]")).perform()
        #driverActionChains.click(self.driver.find_element(By.XPATH, "//span[@title='软件测试与质量控制']")).perform()

        driverWait.until_not(lambda a:a.find_element(By.ID, "el-loading-mask"))     #等待遮罩消失
        self.driver.find_element(By.CLASS_NAME, "list-title").click()       #点击第一条筛选结果
        self.driver.switch_to.window(self.driver.window_handles[len(self.driver.window_handles) - 1])       #切换浏览器窗口
        driverWait.until(lambda a: a.find_element(By.CLASS_NAME, "main_color").is_displayed())  # 等待页面加载
        typeElement = self.driver.find_elements(By.XPATH, "//a[@class='main_color']")  # 获取分类信息
        print("====================验证测试结果====================")
        print("筛选 %s—>%s—>%s 的结果，第一条结果《%s》的分类为：%s" % (title[0], title[1], title[2], text, title[2]))
        bearfruit = False
        for typeName in typeElement:
            if typeName.text.strip() == title[2]:
                bearfruit = True
                break

        assert bearfruit

    """
    @pytest.mark.parametrize('url, waitTime, text, title', CaseData.filter_dataTwo)
    def test_article_filter(self, url, waitTime, text, title):
        driverWait = WebDriverWait(self.driver, waitTime)
        driverActionChains = ActionChains(self.driver)
        self.driver.get(url)
        driverWait.until(lambda a:a.find_element(By.CLASS_NAME, "tabbar-link").is_displayed())
        self.driver.find_element(By.XPATH, "//div[@class='header-item']/span[text()='"+text+"']").click()
        driverWait.until(lambda a:a.find_element(By.ID, "pagesBottom").is_displayed())
        for i in range(1, 4):
            driverActionChains.move_to_element(
                self.driver.find_element(By.XPATH, "(//div[@class='select-box_item--title'])["+str(i)+"]")).perform()
            driverActionChains.click(self.driver.find_element(By.XPATH, "//span[@title='"+title[i - 1]+"']")).perform()

        self.driver.find_element(By.CLASS_NAME, "list-title").click()
        self.driver.switch_to.window(self.driver.window_handles[len(self.driver.window_handles) - 1])
        driverWait.until(lambda a:a.find_element(By.CLASS_NAME, "course-details").is_displayed())
        typeElement = self.driver.find_element(By.XPATH, "//a[@class='main_color']")
        print("====================验证测试结果====================")
        print("筛选 %s—>%s—>%s 的结果，第一条结果《%s》的分类为：%s" %(title[0], title[1], title[2], text, title[2]))
        bearfruit = False
        if typeElement.text in title[2]:
            bearfruit = True

        assert bearfruit
    """