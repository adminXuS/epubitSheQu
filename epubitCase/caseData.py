"""
测试数据
"""
#coding = utf-8
from epubitCase.config import Config

class CaseData:
    Select_class_case = (Config.url, Config.waitTime, "课程", "Java")
    Select_book_case = (Config.url, Config.waitTime, "图书", "Selenium")
    Select_special_case = (Config.url, Config.waitTime, "专栏", "测试")

    epubitCase_data = [Select_book_case, Select_class_case, Select_special_case]

    type = ["软件开发", "软件工程与方法", "软件测试与质量控制"]
    type1 = ["软件开发", "编程语言", "C语言"]
    filter_data = [(Config.url, Config.waitTime, "图书", type1),
                   (Config.url, Config.waitTime, "电子书", type),
                   (Config.url, Config.waitTime, "课程", type),
                   (Config.url, Config.waitTime, "书课包", type1)]
