# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 22:40:39 2018

@author: DELL
"""
import pandas as pd
#读取数据
detail1=pd.read_table('Data/ele_loss.csv',sep=',',encoding='gbk')
detail2=pd.read_table('Data/alarm.csv',sep=',',encoding='gbk')
#查看两表的形状
print('ele_loss表的形状为：',detail1.shape)
print('alarm表的形状为：',detail2.shape)
#以ID和date两个键值作为主键进行内连接
##将ID和date转化为字符串格式，为合并做准备
detail1['ID']=detail1['ID'].astype('str')
detail1['date']=detail1['date'].astype('str')
detail2['ID']=detail2['ID'].astype('str')
detail2['date']=detail2['date'].astype('str')
##进行内连接
detail1_detail2=pd.merge(detail1,detail2,on=['ID','date'])
print('两表主键合并后的形状为：',detail1_detail2.shape)
print('两表主键合并后的数据为：\n',detail1_detail2)



