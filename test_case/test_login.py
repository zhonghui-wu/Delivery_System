#-*- coding: utf-8 -*-
#@File    : test_login.py
#@Time    : 2021/5/28 20:24
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/5/28
import pytest,allure,os
from libs.login import Login
from tools.excelControl import get_excel_data
from tools.yamlControl import get_yaml_caseData
from configs.config import projectPath
from tools.logBasic import logger
log = logger()
import traceback
#定义测试类
@allure.epic("点餐系统")#项目级别
@allure.feature("登录模块")#模块级别
@pytest.mark.Login#mark 标签
class TestLogin:
    #写测试方法
    #数据驱动  ----[(1,2),(3,4)]
    @pytest.mark.parametrize('caseTitle,inBody,expData',get_excel_data('../data/testCaseFile_V1.5.xls',"登录模块","Login",
                          "标题","请求参数","响应预期结果"))
    # @pytest.mark.parametrize('caseTitle,inBody,expData',get_excel_data(projectPath+'/data/testCaseFile_V1.5.xls',"登录模块","Login",
    #                      "标题","请求参数","响应预期结果"))
    #@pytest.mark.parametrize('caseTitle,inBody,expData',get_yaml_caseData(projectPath+'/data/data.yaml'))
    @allure.story("登录接口")#接口级别
    @allure.title("{caseTitle}")#用例级别
    @pytest.mark.login  # mark 标签
    def test_login(self,caseTitle,inBody,expData):
        #allure 增加selenium截图的操作
        allure.attach.file('../data/123.png','登录的截图',
                           attachment_type=allure.attachment_type.PNG)

        print('---登录接口正在运行---')
        try:
            res = Login().login(inBody)  # 1- 调用登录的接口函数
            assert res['msg'] == expData['msg0']#断言：预期与实际相比较，一致返回真，不一致-假
        except Exception as err:#异常处理
            log.error(traceback.format_exc())#具体的报错信息
            raise err#  需要抛出异常给pytest--报告需要体现！

    """
    pytest在控制台输出的信息一些标识：
    .  表示该用例执行成功！
    F 表示该用例执行失败！
    E 语法错误
    """



if __name__ == '__main__':
    #--clean-alluredir  清除数据！
    pytest.main(['test_login.py','-s','--alluredir','../report/tmp'])# -s 打印print信息
    os.system('allure serve ../report/tmp')
    """
    运行一个报告需要什么？需要报告的源数据
    原理：
        1- 使用pytest框架运行后产生测试结果数据
            - 需要把数据存放一个路径
            --alluredir      ../report/tmp
        2- 使用allure工具去解析这个源数据--展示出来效果
            os.system("cmd命令行")
        3- 这个allure  serve 是一个服务，
        4- 最好使用火狐浏览器，设置默认浏览器
    """



