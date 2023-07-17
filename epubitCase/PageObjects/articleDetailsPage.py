"""
筛选结果详情页
"""
#coding = utf-8

from epubitCase.BaseLayer.executorBase import ExecutorBase
from epubitCase.PageObjects.siteHeader import SiteHeader

class ArticleDetailsPage(SiteHeader, ExecutorBase):
    # 遮罩元素
    def filter_loadingMask(self):
        return self.get_element("class", "main_color")

    # 分类信息
    def typeData(self):
        return self.get_elements('xpath', "//a[@class='main_color']")
