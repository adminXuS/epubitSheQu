#coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class ExecutorBase:
    def __init__(self, executor = None, url = None):
        if executor is None:
            self.__init__executor()
        else:
            self.driver = executor

        if url is not None:
            self.driver.get(url)
    #初始化执行器
    def __init__executor(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    #获取测试执行器
    def get_executor(self):
        return self.driver
    #注销测试执行器
    def quit_executor(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None
    #生成元素定位
    def __get__locator(self, keys):
        if keys.lower() == "id":
            return By.ID
        elif keys.lower() == "name":
            return By.NAME
        elif keys.lower() == "class":
            return By.CLASS_NAME
        elif keys.lower() == "xpath":
            return By.XPATH
        elif keys.lower() == "link":
            return By.LINK_TEXT
        elif keys.lower() == "css":
            return By.CSS_SELECTOR
    #查找单个元素
    def get_element(self, key, value):
        return self.driver.find_element(self.__get__locator(key), value)
    #查找多个元素
    def get_elements(self, key, value):
        return self.driver.find_elements(self.__get__locator(key), value)
    #等待元素消失
    def wait_for_element_until_not(self, get_element_func, seconds = 5):
        WebDriverWait(self.get_executor(), seconds).until_not(lambda d: get_element_func)
    #等待元素出现
    def wait_for_element_until(self, get_element_func, seconds = 5):
        WebDriverWait(self.get_executor(), seconds).until(lambda d: get_element_func.is_displayed())
    #子元素
    def get_element_in(self, get_elements, key, value):
        return get_elements.find_element(self.__get__locator(key), value)
    #切换浏览器句柄
    def switch_to_window(self):
        lastWindowIndex = len(self.get_executor().window_handles) - 1
        self.get_executor().switch_to.window(self.get_executor().window_handles[lastWindowIndex])
    #点击操作
    def get_click_element(self, elementData):
        elementData.click()
    #输入操作
    def get_send_keys_element(self, elementData, word):
        elementData.send_keys(word)
