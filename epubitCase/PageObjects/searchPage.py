"""
搜索页——元素
"""
#coding = utf-8

from epubitCase.PageObjects.siteHeader import SiteHeader

class SearchPage(SiteHeader):
    # 搜索页——搜索框元素
    def inputElement(self):
        return self.get_element("class", "el-input__inner")

    # 搜索页——搜索产品元素
    def selectProduct(self):
        return self.get_element("class", "is-plain")

    # 等待搜索结果出现
    def searchResult(self):
        return self.get_element("class", "el-input__inner")