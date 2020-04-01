# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 23:12:01 2018

@author: DELL
"""
import pandas as pd
#读取csv数据
detail=pd.read_csv('Data/Training_Master.csv',encoding='gbk')
#查看维度、大小、占用内存信息
print('主表的维度为：',detail.ndim)
print('主表的大小（形状）为：',detail.shape)
print('主表的占用内存为：\n',detail.memory_usage)
#使用describe方法进行描述性统计（整体）
print('主表的描述性统计结果为：\n',detail.describe())
#使用describe方法进行描述性统计（数值型数据）
print('主表中WeblogInfo_4与ThirdParty_Info_Period2_13(数值型数据)的描述性统计结果为：\n',detail[['WeblogInfo_4','ThirdParty_Info_Period2_13']].describe())
#使用describe方法进行描述性统计（类别型数据）
detail['Idx']=detail['Idx'].astype('category')
detail['UserInfo_2']=detail['UserInfo_2'].astype('category')
print('主表中Idx与UserInfo_2（类别型数据）的描述性统计结果为：\n',detail[['Idx','UserInfo_2']].describe())
#剔除值相同或全为空的列
def dropNullStd(data):#定义一个函数剔除值全为空和标准差为0的列
    beforelen=data.shape[1]
    colisNull=data.describe().loc['count']==0
    for i in range(len(colisNull)):
        if colisNull[i]:
            data.drop(colisNull.index[i],axis=1,inplace=True)
    stdisZero=data.describe().loc['std']==0
    for i in range(len(stdisZero)):
        if stdisZero[i]:
            data.drop(stdisZero.index[i],axis=1,inplace=True)
    afterlen=data.shape[1]
    print('剔除值相同或全为空的列的数目为：',beforelen-afterlen)
    print('剔除值相同或全为空的列后的数据的形状为：',data.shape)
dropNullStd(detail)#使用dropNullStd函数对主表进行操作
    



