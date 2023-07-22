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
from epubitCase.PageObjects.articleListPage import ArticleListPage
from epubitCase.PageObjects.articleDetailsPage import ArticleDetailsPage
from epubitCase.PageObjects.homePage import HomePage
from epubitCase.PageObjects.filterCategory import FilterCategory
from config import Config

class Test_epubit_filter():
    def setup_method(self):
        homeUrl = Config.url
        self.homePage = HomePage(url= homeUrl)
        self.filterCategory = FilterCategory(executor= self.homePage.get_executor())
        self.articleListPage = ArticleListPage(executor= self.homePage.get_executor())
        self.articleDetailsPage = ArticleDetailsPage(executor= self.homePage.get_executor())

    def teardown_method(self):
        self.homePage.quit_executor()

    @pytest.mark.parametrize("waitTime, text, title", CaseData.filter_data)
    def test_book_filter(self, waitTime, text, title):
        self.homePage.wait_for_element_until(self.homePage.searchGuide(text), seconds= waitTime)
        self.homePage.get_click_element(self.homePage.searchGuide(text))
        self.homePage.wait_for_element_until(self.filterCategory.searchRegion(), seconds= waitTime)
        for i in range(0, 3):
            self.homePage.get_action_chains("move", self.filterCategory.searchType(i + 1))
            self.homePage.get_action_chains("click", self.filterCategory.typeElement(title[i]))
            time.sleep(1)
        self.homePage.wait_for_element_until_not(self.filterCategory.filter_loadingMask(), seconds= waitTime)  # 等待遮罩消失
        self.homePage.get_click_element(self.articleListPage.selectBearfruit())  # 点击第一条筛选结果
        self.homePage.switch_to_window()  # 切换浏览器窗口
        self.homePage.wait_for_element_until(self.articleDetailsPage.filter_loadingMask(), seconds= waitTime)  # 等待页面加载
        typeElement = self.articleDetailsPage.typeData()  # 获取分类信息
        print("====================验证测试结果====================")
        print("筛选 %s—>%s—>%s 的结果，第一条结果《%s》的分类为：%s" % (title[0], title[1], title[2], text, title[2]))
        bearfruit = False
        for typeName in typeElement:
            if typeName.text.strip() == title[2]:
                bearfruit = True
                break

        assert bearfruit

    """
    @pytest.mark.parametrize('waitTime, text, title', CaseData.filter_data1)
    def test_article_filter(self, waitTime, text, title):
        driver = self.homePage.get_executor()
        driverWait = WebDriverWait(driver, waitTime)
        driverActionChains = ActionChains(driver)
        driverWait.until(lambda a:a.find_element(By.CLASS_NAME, "tabbar-link").is_displayed())
        driver.find_element(By.XPATH, "//div[@class='header-item']/span[text()='"+text+"']").click()
        driverWait.until(lambda a:a.find_element(By.ID, "pagesBottom").is_displayed())
        for i in range(0, 3):
            driverActionChains.move_to_element(
                driver.find_element(By.XPATH, "(//div[@class='select-box_item--title'])["+str(i + 1)+"]")).perform()
            driverActionChains.click(driver.find_element(By.XPATH, "//span[@title='"+title[i]+"']")).perform()
            time.sleep(1)
        driverWait.until_not(lambda a:a.find_element(By.ID, "el-loading-mask"))
        driver.find_element(By.CLASS_NAME, "list-title").click()
        driver.switch_to.window(driver.window_handles[len(driver.window_handles) - 1])
        driverWait.until(lambda a:a.find_element(By.CLASS_NAME, "main_color").is_displayed())
        typeElement = driver.find_elements(By.XPATH, "//a[@class='main_color']")
        print("====================验证测试结果====================")
        print("筛选 %s—>%s—>%s 的结果，第一条结果《%s》的分类为：%s" %(title[0], title[1], title[2], text, title[2]))
        bearfruit = False
        for typeName in typeElement:
            if typeName.text.strip() in title[2]:
                bearfruit = True

        assert bearfruit
    """