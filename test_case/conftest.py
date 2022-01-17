#-*- coding: utf-8 -*-
#@File    : conftest.py
#@Time    : 2021/5/30 11:02
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/5/30
import pytest
"""
@pytest.fixture(scope=)  
scope作用域：
    1- function  方法级别  每一个方法都执行这个fixture 紧跟的函数一次
    2- class 类级别 每一个类都执行这个fixture 紧跟的函数  一次
    3- module 模块级别 每一个py模块都执行这个fixture 紧跟的函数  一次
    4- session 包级别 每一个包都执行这个fixture 紧跟的函数  一次
    
autouse:是否自动运行！  bool类型


"""
from libs.login import Login
from libs.shop import Shop
import os
@pytest.fixture(scope="session",autouse=True)
def start_running():
    #开始 setup
    print("---点餐系统*接口自动化开始运行---")
    print("---清除报告数据---")
    #删除多余的上一次报告的数据
    try:
        for one in os.listdir('../report/tmp'):
            if '.json' in one or '.txt' in one:
                os.remove(f'../report/tmp/{one}')
    except:
        pass


    #teardown
    yield
    print("---点餐系统*接口自动化结束运行---")




# @pytest.fixture(scope="class")#手动调用
# def xt_test1():
#     print("---xt_test——1---")
#
# @pytest.fixture(scope="class")#手动调用
# def xt_test2():
#     print("---xt_test——2---")
"""
pytest的fixture用法：作为环境初始化操作/数据清除
    1- 没有返回值
        场景：只管执行，不需要关心是否有返回值
        使用：你需要在什么地方使用，直接调用 
            @pytest.mark.usefixtures("函数名称")#手动fixture
        加强版场景：
            可以叠加----自下往上运行  fixture函数
            
    2- 有返回值：
        场景：当我们一些前置条件，执行后需要获取对应的执行结果（返回值）
            这个前置条件的结果，是后续接口的入参（关联参数）
        使用：在对应的fixture最后使用return  返回你需要的返回值

"""
#1--====登录初始化操作---获取token---  前置条件
@pytest.fixture(scope="class")#手动调用
def login_init():
    # 1- 登录操作--获取token
    token = Login().login({"username": "sq0777", "password": "xintian"}, getToken=True)
    return token#返回值

#2--====店铺初始化操作---获取店铺实例---  前置条件
@pytest.fixture(scope="class")#手动调用
def shop_init(login_init):#去使用前面定义的fixture函数名，就是使用他的返回值
    # 创建店铺实例
    shopObject = Shop(login_init)
    print("---我正在初始化店铺实例---")

    yield  shopObject #teardown  数据清除操作
    # 数据清除操作
    print("---我结束店铺实例---")

    #return shopObject#返回值--店铺实例

#3--====店铺更新接口操作---获取店铺实例、id  图片信息---  前置条件
@pytest.fixture(scope="function")#手动调用
def update_shop_init(shop_init):#去使用前面定义的fixture函数名，就是使用他的返回值
    # 创建店铺实例
    shopID = shop_init.shop_list({"page":1,"limit":10})["data"]["records"][0]["id"]
    imageInfo = shop_init.file_upload("123.png","image/png")
    print("---我正在初始化update_shop_init---")
    return shop_init,shopID,imageInfo#返回值--获取店铺实例、id  图片信息