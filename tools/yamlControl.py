#-*- coding: utf-8 -*-
#@File    : yamlControl.py
#@Time    : 2021/6/2 20:15
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/6/2
import yaml
def get_yaml_data(fileName):#只能读取一个yaml
    #1- 把yaml在内存里打开
    fo = open(fileName,'r',encoding='utf-8')
    #2- 调用yaml库函数
    res = yaml.load(fo,Loader=yaml.FullLoader)
    return res


#读取yaml多段文件 ---
def get_yamls_data(fileName):#只能读取一个yaml
    resList = []#存放结果
    #1- 把yaml在内存里打开
    fo = open(fileName,'r',encoding='utf-8')
    #2- 调用yaml库函数
    res = yaml.load_all(fo,Loader=yaml.FullLoader)
    print(res,type(res))
    for one in res:
        resList.append(one)
    return resList

#3- 获取yaml测试用例数据
def get_yaml_caseData(fileName):#只能读取一个yaml
    resList = []#放结果数据！
    #1- 把yaml在内存里打开
    fo = open(fileName,'r',encoding='utf-8')
    #2- 调用yaml库函数
    res = yaml.load(fo,Loader=yaml.FullLoader)
    #3- 你的当前的方案res[0]是公共数据--暂时不需要
    del res[0]
    for one in res:
        resList.append((one['detail'],one['data'],one['resp']))
    return resList


#写yaml数据
def set_yaml_data(fileName,inData):
    #1- 把yaml在内存里打开
    fo = open(fileName,'w',encoding='utf-8')
    #2- 调用yaml库函数
    yaml.dump(inData,fo)
    fo.close()#关闭文件



"""
场景：在我们一些脚本迭代或优化的时候，有时候需要替换方案
设计方案：
    1- 下游接收方，需要什么样式的数据
        - 是对应的测试方法中的数据驱动使用了用例数据
        - [(标题2，请求body1，响应数据1)，(标题2，请求body2，响应数据2)]
    
    2- 新方案的技术方向要跟下游方的数据格式一直！
"""

if __name__ == '__main__':
    res = get_yaml_data('../configs/conf.yaml')
    print(res)


