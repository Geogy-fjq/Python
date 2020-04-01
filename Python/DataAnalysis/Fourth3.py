# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 14:24:44 2018

@author: DELL
"""
import pandas as pd
import numpy as np
#读取数据
detail1=pd.read_table('Data/Training_Userupdate.csv',sep=',',encoding='gbk')#读取用户信息更新表数据
detail2=pd.read_table('Data/Training_LogInfo.csv',sep=',',encoding='gbk')#读取登录信息表数据
#对表进行分组
detail1['Update']=pd.to_datetime(detail1['UserupdateInfo2'])#转换时间字符串
detail2['Land']=pd.to_datetime(detail2['LogInfo3'])
detailGroup1=detail1[['Idx','Update']].groupby(by='Idx')#对用户信息更新表进行分组
detailGroup2=detail2[['Idx','Land']].groupby(by='Idx')#对登录信息表进行分组
print('分组后的用户信息更新表为：',detailGroup1)
print('分组后的登录信息表为：',detailGroup2)

#求出分组后最早和最晚的更新和登录时间
print('分组后最早和最晚的更新时间分别为：\n',detailGroup1.agg([np.min,np.max]))#更新时间
print('分组后最早和最晚的登录时间分别为：\n',detailGroup2.agg([np.min,np.max]))#登录时间
#求出分组后的数据更新和登录次数
print('分组后的数据更新次数为：\n',detailGroup1.size())#更新次数
print('分组后的数据登录次数为：\n',detailGroup2.size())#登录次数
