#coding = utf-8

import pytest
import os

if __name__ == "__main__":
    # pytest执行脚本并生成测试结果文件到report/tmp目录下
    pytest.main("-s", "--alluredir", "allure-report\\tmp")


    # 将report/tmp目录下的结果文件生成html类型的测试报告文件到report/html目录下
    # -o report/html --clean 是为了清空已有的测试报告再生成
    os.system(r'allure generate allure-report\\tmp -o allure-report/html --clean')