# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 22:41:44 2018

@author: DELL
"""
import pandas as pd
from scipy.interpolate import lagrange
#读取数据
detail=pd.read_table('Data/missing_data.csv',sep=',',encoding='gbk')
#查询缺失值所在的位置
print('missing_data中缺失值所在的位置为：\n',detail[detail.isnull().values==True])
#拉格朗日插值
##定义拉格朗日插值函数
def interp_lagrange(r,c,k=2): #k=2：用空值的前后2个数值来拟合曲线和预测空值
    y = r[list(range(c-k,c)) + list(range(c+1,c+1-k))] #取值
    y = y[y.notnull()]#保证y的数值都非空
    return lagrange(y.index,list(y))(c) #调用拉格朗日函数
##逐个元素判断是否需要插值
for i in detail.columns: 
    for j in range(len(detail)):
        if (detail[i].isnull())[j]:#如果detail[i][j]为空，调用函数interp_lagrange为其插值
            detail[i][j] = interp_lagrange(detail[i],j)
#查看数据中是否存在缺失值
print("每个特征缺失的数目为（拉格朗日插值完成，查看数据中是否存在缺失值）：\n",detail.isnull().sum())
