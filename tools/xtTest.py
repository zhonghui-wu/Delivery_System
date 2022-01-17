#-*- coding: utf-8 -*-
#@File    : xtTest.py
#@Time    : 2021/6/6 9:35
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/6/6 
print()
import time

"""
需求：现在领导需要我们对每一个函数进行计时！
具体要求：不能改变调用方式
"""

#-----------方案v1--小明---------------
"""
方案描述：
    1- 太简单，直接在test函数里增加  
        startTime = time.time()  endTime=xxx
def test():
    #模拟执行过程--sleep()
    startTime = time.time()
    print("---开始执行自动化操作---")
    time.sleep(1)
    print("---结束执行自动化操作---")
    endTime = time.time()
    print("总共耗时>>> ",endTime-startTime)
讨论结果：这个方案不合理
    原因：代码修改量太大，后续其他的需求不好维护！
"""
#-----------方案v2--小青---------------
"""
方案：
    1- 不修改原有的代码
    2- 自己新增加一个需要函数
验证测试：
    1- 是没有修改原有的函数结构
    2- 功能也实现了
    3- 以前的我执行是test()调用方式，小青修改后，他直接修改了执行方式
"""
# def show_time(func):
#     startTime = time.time()
#     #执行那个函数
#     func()#函数调用
#     endTime = time.time()
#     print("总共耗时>>> ",endTime-startTime)

# if __name__ == '__main__':
#     show_time(test)#test  一个函数对象--函数名

#--------------方案v3----------------
"""
需求梳理:
    1- 不能修改原函数的内容
    2- 不能改变原函数调用方式
方案：
    增加需求，又不能改原函数代码，也不能修改调用方式---？
    python--装饰器--可以实现以上操作！
    
#闭包：
    在一个函数里定义一个函数，内置函数使用了外函数的一个变量,
    外函数的返回值是内函数的函数对象(函数名)
"""
# def show_time(func):
#     def inner():
#         startTime = time.time()
#         #执行那个函数
#         func()#函数调用
#         endTime = time.time()
#         print("总共耗时>>> ",endTime-startTime)
#     return inner
#
#
# #目前的代码--很多自动化函数
# @show_time# test = show_time(test)
# def test():
#     #模拟执行过程--sleep()
#     print("---开始执行自动化操作-test--")
#     time.sleep(1)
#     print("---结束执行自动化操作-test--")
#     endTime = time.time()
#
# @show_time# test2 = show_time(test2)
# def test2():
#     #模拟执行过程--sleep()
#     print("---开始执行自动化操作-test2--")
#     time.sleep(1)
#     print("---结束执行自动化操作-test2--")
#     endTime = time.time()
#
# if __name__ == '__main__':
#     #test = show_time(test)#show_time(test) 返回一个inner函数对象，
#     # 把inner函数对象  赋值给一个与test同名的变量---  test == inner
#     #  test() == inner()
#     #test()#test() == inner()
#
#     #test2 = show_time(test2)
#     test()
#     test2()

#----------------------带参数的-------------
def show_time(func):
    def inner(*a):
        startTime = time.time()
        #执行那个函数
        res = func(*a)#函数调用
        endTime = time.time()
        print("总共耗时>>> ",endTime-startTime)
        return res#  这个是func返回值
    return inner


#目前的代码--很多自动化函数
@show_time# test = show_time(test)
def test(*a):
    #模拟执行过程--sleep()
    print("---开始执行自动化操作-test--",a)
    time.sleep(1)
    print("---结束执行自动化操作-test--")
    endTime = time.time()


if __name__ == '__main__':
    res = test(100,200)
    print(res)
