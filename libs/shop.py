#-*- coding: utf-8 -*-
#@File    : shop.py
#@Time    : 2021/5/30 9:08
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/5/30
#这个代码只是一个业务层代码
#店铺里每一个接口都需要token--能不能再这个类的初始化方法增加token
from configs.config import HOST
from libs.login import Login
from configs.config import projectPath
import requests
class Shop:
    def __init__(self,inToken):
        self.header = {"Authorization":inToken}#请求头参数

    #1-列出接口
    def shop_list(self,inData):
        #url
        url = f"{HOST}/shopping/myShop"
        #请求数据
        payload = inData
        #请求
        resp = requests.get(url,params=payload,headers=self.header)
        return resp.json()#字典数据



    def file_upload(self,fileName,fileType):#图片上传接口
        url = f"{HOST}/file"
        """
        请求体构建--有点难度
            键：
                -接收文件的变量
            值：
                -文件名
                -文件对象---open(文件路径，打开模式)--rb
                -文件类型  
        """
        #userFile = {"file":(fileName,open(projectPath+f"/data/{fileName}","rb"),fileType)}#绝对路径
        userFile = {"file": (fileName, open(f"../data/{fileName}", "rb"), fileType)}  # 绝对路径
        resp = requests.post(url,files=userFile,headers=self.header)
        return resp.json()["data"]["realFileName"]

    #2-编辑店铺
    """
    编辑店铺：
        1- 店铺的id--必填----这个数据从列出店铺接口获取！---动态
        2- 图片信息---选填---这个数据从图片上传接口获取！---动态
    """
    def shop_update(self,inData,shopId,imageInfo):
        """
        :param inData: 请求数据
        :param shopId: 店铺id
        :param imageInfo: 图片信息
        :return: 响应数据
        """
        #url
        url = f"{HOST}/shopping/updatemyshop"
        #请求数据
        #扩展思路：
        # if inData["id"] == "SHOPID":#  标识--这个用例数据需要动态获取真实id
        #     inData["id"] = shopId
        inData["id"] = shopId
        inData["image_path"] = imageInfo
        inData["image"] = f"/file/getImgStream?fileName={imageInfo}"
        resp = requests.post(url,data=inData,headers=self.header)
        return resp.json()
        #请求



if __name__ == '__main__':
    #1- 登录操作--获取token
    token = Login().login({"username":"sq0777","password":"xintian"},getToken=True)
    #2- 调用列出接口
    shopObject = Shop(token)
    res = shopObject.shop_list({"page":1,"limit":10})

    shopID = res["data"]["records"][0]["id"]
    print(shopID)

    #3- 调用图片接口
    imageInfo = shopObject.file_upload("123.png","image/png")
    print(imageInfo)

    #4- 编辑接口
    testData ={
            "name": "心田星巴克新建店",
            "address": "上海市静安区秣陵路303号",
            "id": "3269",
            "Phone": "13176876632",
            "rating": "5.0",
            "recent_order_num":100,
            "category": "快餐便当/简餐",
            "description": "满30减5，满60减8",
            "image_path": "b8be9abc-a85f-4b5b-ab13-52f48538f96c.png",
            "image": "http://121.41.14.39:8082/file/getImgStream?fileName=b8be9abc-a85f-4b5b-ab13-52f48538f96c.png"
        }

    res2 = shopObject.shop_update(testData,shopID,imageInfo)
    print(res2)


