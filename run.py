#-*- coding: utf-8 -*-
#@File    : run.py.py
#@Time    : 2021/6/2 20:39
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/6/2
print()
"""
用户可以自行修运行模式
    1- 可以做配置文件
    2- 不懂自动化测试的人员，可以修改对应的模式
方案：
    1- run.py
    2- config.yaml
"""
import pytest,os
from tools.yamlControl import get_yaml_data
if __name__ == '__main__':
    #1- 获取配置文件数据
    res = get_yaml_data('configs/config.yaml')#字典
    print(res)
    #2- 调用配置文件执行
    pytest.main(res['runParams'])#res['runParams']  运行参数
    os.system(' '.join(res['reportParams']))#res['reportParams']报告参数


# #[1,2,3]
# '-'.join([1,2,3])#1-2-3