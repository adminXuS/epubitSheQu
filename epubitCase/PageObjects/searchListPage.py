"""
搜索书籍结果列表页面元素模块
"""
#coding = utf-8

from epubitCase.PageObjects.siteHeader import SiteHeader

class SearchListPage(SiteHeader):
    """
    继承 ExecutorBase 模块后，不需要初始化函数
    def __init__(self, driver):
        self.driver = driver
    """
    # 搜索结果页——搜索类型元素
    def changeType(self, type):
        return self.get_element("xpath", "//div[@class='tabs']/span[text()='" + type + "']")

    # 搜索结果页——搜索结果元素
    def selectResult(self):
        return self.get_elements("class", "mode1")

    # 搜索结果页——产品名称元素
    def productName(self, resultElement):
        return self.get_element_in(resultElement, "class", "list-title").text

    # 遮罩元素
    def filter_loadingMask(self):
        return self.get_elements("id", "el-loading-mask")
