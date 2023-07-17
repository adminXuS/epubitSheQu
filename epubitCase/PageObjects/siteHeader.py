"""
首页——页眉公共区域
"""
#coding = utf-8

from epubitCase.BaseLayer.executorBase import ExecutorBase

class SiteHeader(ExecutorBase):
    # 首页——放大镜元素
    def selectElement(self):
        return self.get_element("class", "main_border")

    # 首页导航栏
    def searchGuide(self, text):
        return self.get_element('xpath', "//div[@class='header-item']/span[text()='" + text + "']")