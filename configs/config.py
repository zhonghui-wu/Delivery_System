#-*- coding: utf-8 -*-
#@File    : config.py
#@Time    : 2021/5/30 9:19
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/5/30
import os,sys
HOST = "http://121.41.14.39:8082"
projectName = "Delivery_System-0523"#如果自己有好的方案，可以自行调试！
#print(__file__)#当前路径
#print(os.path.realpath(__file__))
print(sys.argv[0])#当前文件路径
projectPath = sys.argv[0].split(projectName)[0]+projectName
print(projectPath)