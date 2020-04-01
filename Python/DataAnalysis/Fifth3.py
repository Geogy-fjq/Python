# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 22:40:48 2018

@author: DELL
"""
import pandas as pd
#读取数据
detail=pd.read_table('Data/model.csv',sep=',',encoding='gbk')
#定义标准差标准化函数
def StandardScaler(data):
    data=(data-data.mean())/data.std()
    return data
#使用函数分别对3列数据进行标准化
data1=StandardScaler(detail['电量趋势下降指标'])
data2=StandardScaler(detail['线损指标'])
data3=StandardScaler(detail['告警类指标'])
data=pd.concat([data1,data2,data3],axis=1)
#查看标准化后的数据
print('标准差标准化后的数据为：\n',data)
