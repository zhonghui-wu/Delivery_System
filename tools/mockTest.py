#-*- coding: utf-8 -*-
#@File    : mockTest.py
#@Time    : 2021/6/4 20:32
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/6/4
import requests
HOST = 'http://127.0.0.1:9999'
# def test():
#     #1- url
#     url = f'{HOST}/sq'
#     payload = {	"key1":"abc"}
#     #发请求
#     resp = requests.post(url,data=payload)
#     return resp.text
#
# if __name__ == '__main__':
#     res = test()
#     print(res)

#1- 申请订单提交接口
def create_order(inData):
    url = f'{HOST}/api/order/create/'
    payload = inData
    resp = requests.post(url,json=payload)
    return resp.json()


#2- 查询申请结果接口
"""
查询接口注意事项：
    1- 你使用什么去查询---申请的id
    2- 频率  interval
    3- 如果查询不到--超时 timeout
"""
import time
def get_order_result(orderID,interval=5,timeout=30):#单位是s
    """
    :param orderID: 申请的id
    :param interval: 频率 默认是5s
    :param timeout: 超时时间 30s
    :return:
    """
    url = f'{HOST}/api/order/get_result01/'
    payload = {"order_id": orderID}#
    #1- 记录开始的时间
    startTime = time.time()
    #2- 结束时间:开始时间+超时时间
    endTime = startTime+timeout
    cnt = 0#计算查询的次数
    #3- 循环发请求：while
    while time.time()<endTime:#当前时间< 结束时间
        resp = requests.get(url, params=payload)
        cnt += 1#

        if resp.text:#更加精准的判断是返回有效数据
            print(f"第{cnt}次查询，已经有结果，停止查询！",resp.text)
            break
        else:
            print(f"第{cnt}次查询，没有结果，请等待！")
        time.sleep(interval)  # 等待！
    print("---查询结束！---")

    return resp.text

import threading#多线程模块--自带的

if __name__ == '__main__':
    startTime = time.time()#所有接口运行的开始时间
    #测试数据
    testData = {
        "user_id": "sq123456",
        "goods_id": "20200815",
        "num": 1,
        "amount": 200.6
    }
    #2- 调用提交申请请求--获取申请的id
    id = create_order(testData)['order_id']
    print(id)
    #后面是其他的接口的自动化执行操作
    for one in range(20):
        time.sleep(1)#模拟下接口自动化测试的操作过程
        print(f"{one}----我正在执行其他的接口的自动化执行操作----")
    endTime = time.time()  # 所有接口运行的开始时间

    print(f"整个项目自动化测试完成，总耗时>>>{endTime-startTime}")#----80s
    """
    创建子线程：
    threading.Thread(target,args)
    target  你需要把哪一个函数作为子线程执行，就把对应的函数名赋值给这个参数
    args：这个函数，调用调用的时候，需要传递是么参数--参数的参数 ---元组类型
    """
    t1 = threading.Thread(target=get_order_result,args=(id,))#创建子线程：

    #主线程如果结束了/或者异常退出运行，子线程也应该直接退出！
    #t1.setDaemon(True)#守护线程
    #启动子线程
    t1.start()
    t1.join()  # 阻塞，主线程运行完之前，会等到所有的 子线程结束再主线结束
    # res2 = get_order_result(id)
    # print(res2)


    # #后面是其他的接口的自动化执行操作
    # for one in range(20):
    #     time.sleep(1)#模拟下接口自动化测试的操作过程
    #     print(f"{one}----我正在执行其他的接口的自动化执行操作----")
    # endTime = time.time()  # 所有接口运行的开始时间
    #
    # print(f"整个项目自动化测试完成，总耗时>>>{endTime-startTime}")#----80s



"""
问题：
    你的领导看到你的自动化测试非常的欣慰，但是在欣慰过后，
        有一个小需求，能不能提高下执行效率---
方案分析：
    1- 领导看到的是表面的一个现象
    2- 慢的根本原因：运行机制问题---time.sleep(5)
    3- 给出方案：
        1- requests.xx（）和sleep（）----io阻塞模式
        2- 采取多线程操作
            1- 主线程---mian  主线程
            2- 子线程---get_order_result
"""


