"""
类别筛选公共区域
"""
#coding = utf-8

from epubitCase.BaseLayer.executorBase import ExecutorBase

class FilterCategory(ExecutorBase):
    # 筛选块元素
    def searchRegion(self):
        return self.get_element('id', "pagesBottom")

    # 筛选分类选择框元素
    def searchType(self, number):
        return self.get_element('xpath', "(//div[@class='select-box_item--title'])[" + str(number) + "]")

    # 选择分类元素
    def typeElement(self, test):
        return self.get_element('xpath', "//span[@title='" + test + "']")

    # 遮罩元素
    def filter_loadingMask(self):
        return self.get_elements("id", "el-loading-mask")