#-*- coding: utf-8 -*-
#@File    : login.py
#@Time    : 2021/5/28 20:12
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/5/28 
import requests,hashlib
from configs.config import HOST
from tools.xtTest import show_time
def get_md5(psw):#加密函数
    #1- 实例化  一个md5对象
    md5 = hashlib.md5()
    #2- 调用加密方法
    md5.update(psw.encode("utf-8"))
    #3- 返回加密后结果
    return md5.hexdigest()#16进制

class Login:
    #@show_time

    def login(self,inData,getToken=False):
        """
        :param inData: 账号密码
        :param getToken: 是否获取token值，默认值是false不获取token
        :return:
        """
        #1- url
        url = f"{HOST}/account/sLogin"
        #2- 请求头--可以省略
        #3- 请求体
        inData["password"] = get_md5(inData["password"])#字典修改值
        payload = inData
        #4- 发送请求
        resp = requests.post(url,data=payload)
        #
        # print("获取响应编码>>> ",resp.encoding)
        # #修改编码
        # #resp.encoding = 'utf-8'
        # print("修改过响应编码>>> ", resp.encoding)
        #5- 获取响应数据--响应体数据
        #print(resp.text)#字符串数据
        if getToken:#为真--获取token
            return resp.json()['data']['token']
        else:  #获取响应数据
            return resp.json()#字典数据

"""
登录的方法的作用：
    1- 做登录的接口自动化测试----获取登陆的响应数据
    2- 获取token,后续接口需要这个token
"""

if __name__ == '__main__':
    # res = Login().login({"username":"sq0777","password":"xintian"},getToken=False)
    # print(res)


    #1-编码操作：字符--转化--计算机
    str1 = "hello"
    str2 = str1.encode("gbk")# 字节类型   b''
    print(str2 )

    #解码操作
    str3 = str2.decode("utf-8")
    print(str3)



