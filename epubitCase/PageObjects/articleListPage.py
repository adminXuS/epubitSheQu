"""
筛选列表页元素定位
"""
#coding = utf-8

from epubitCase.BaseLayer.executorBase import ExecutorBase
from epubitCase.PageObjects.siteHeader import SiteHeader
from epubitCase.PageObjects.filterCategory import FilterCategory

class ArticleListPage(SiteHeader, FilterCategory, ExecutorBase):
    # 第一条结果元素
    def selectBearfruit(self):
        return self.get_element('class', "list-title")