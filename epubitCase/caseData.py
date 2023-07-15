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