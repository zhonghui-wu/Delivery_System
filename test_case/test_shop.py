#-*- coding: utf-8 -*-
#@File    : test_shop.py
#@Time    : 2021/5/30 10:39
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/5/30
print()
"""
测试文件：包含用例逻辑--环境初始化与数据清除！
场景说明：
    1- 列出接口--需要提前创建店铺
        方案分类
            1- 如果有创建店铺的接口可以直接调用这个接口创建店铺
            2- 如果很多项目没有这个接口/需要admin权限去操作店铺数据，
                可以使用数据库创建店铺---自动化测试人员需要获取数据权限--脱敏数据操作
    我们项目：
        账号数据--mysql
        店铺数据/订单数据/食品数据  mongodb
"""
"""
问题：
    店铺里每一个测试方法都需要登录操作，如果每个方法都写，很累赘！
解决方案：
    1- 常规的setup初始化操作去实现登录
        描述：
            1- 每一个测试类，都得写登录，虽然可以解决一个类里面
            测试方法不需要重复登录操作，但是如果是多个业务模块，会出现每一个模块的都重复登录
            
    2- pytest专属的初始化操作  fixture
        描述：
            1- 把登录做出一个模块化，需要就调用！
对比结果：
    功能都可以实现，优化方案选择方案二！
"""
import pytest,allure,os
from tools.excelControl import get_excel_data
from configs.config import projectPath
# @pytest.mark.usefixtures("xt_test1")#手动fixture
# @pytest.mark.usefixtures("xt_test2")#手动fixture
@allure.epic("点餐系统")#项目级别
@allure.feature("店铺模块")#模块级别
@pytest.mark.Shop#mark 标签
class TestShop:
    # 1-店铺列出的测试方法
    @pytest.mark.parametrize('caseTitle,inBody,expData',
                             get_excel_data('../data/testCaseFile_V1.5.xls', "我的商铺", "listshopping",
                                            "标题", "请求参数", "响应预期结果"))
    # @pytest.mark.parametrize('caseTitle,inBody,expData',
    #                          get_excel_data(projectPath+'/data/testCaseFile_V1.5.xls', "我的商铺", "listshopping",
    #                                         "标题", "请求参数", "响应预期结果"))
    @allure.story("店铺列出接口")#接口级别
    @allure.title("{caseTitle}")#用例级别
    @pytest.mark.Shop_list  # mark 标签
    def test_shop_list(self,caseTitle,inBody,expData,shop_init):
        #2- 调用店铺的更新接口
        res = shop_init.shop_list(inBody)
        #3- 断言
        if 'code' in res:
            assert res['code'] == expData['code']
        else:
            assert res['error'] == expData['error']

    # 2-店铺更新的测试方法
    @pytest.mark.parametrize('caseTitle,inBody,expData',
                             get_excel_data('../data/testCaseFile_V1.5.xls', "我的商铺", "updateshopping",
                                            "标题", "请求参数", "响应预期结果"))

    #@pytest.mark.parametrize('caseTitle,inBody,expData',
                             # get_excel_data(projectPath+'/data/testCaseFile_V1.5.xls', "我的商铺", "updateshopping",
                             #                "标题", "请求参数", "响应预期结果"))

    @allure.story("店铺更新接口")#接口级别

    @allure.title("{caseTitle}")#用例级别
    @pytest.mark.Shop_update # mark 标签
    def test_shop_update(self,caseTitle,inBody,expData,update_shop_init):
        #2- 调用店铺的更新接口
        res = update_shop_init[0].shop_update(inBody,update_shop_init[1],update_shop_init[2])
        #3- 断言
        assert res['code'] == expData['code']



if __name__ == '__main__':
    #--clean-alluredir  清除数据！
    pytest.main(['test_shop.py','-s','-m','Shop_update','--alluredir','../report/tmp','--clean-alluredir'])# -s 打印print信息
    os.system('allure serve ../report/tmp')