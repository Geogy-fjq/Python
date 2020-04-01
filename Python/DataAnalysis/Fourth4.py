# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 14:24:55 2018

@author: DELL
"""
import pandas as pd
#读取数据
detail1=pd.read_table('Data/Training_Userupdate.csv',sep=',',encoding='gbk')#读取用户信息更新表数据
detail2=pd.read_table('Data/Training_LogInfo.csv',sep=',',encoding='gbk')#读取登录信息表数据
#使用pivot_table函数进行长宽表转换
detailPivot1=pd.pivot_table(detail1, index =['Idx'],columns=['ListingInfo1'],aggfunc='count')
detailPivot2=pd.pivot_table(detail2,index=['Idx'],columns=['Listinginfo1'],aggfunc='count')
print('使用pivot_table函数进行长宽表转换后的表Training_Userupdate为：\n',detailPivot1)
print('使用pivot_table函数进行长宽表转换后的表Training_LogInfo为：\n',detailPivot2)
#使用crosstab函数进行长宽表转换
detailCross1=pd.crosstab(index=detail1['Idx'],columns=detail1['ListingInfo1'])
detailCross2=pd.crosstab(index=detail2['Idx'],columns=detail2['Listinginfo1'])
print('使用crosstab函数进行长宽表转换后的表Training_Userupdate为：\n',detailCross1)
print('使用crosstab函数进行长宽表转换后的表Training_LogInfo为：\n',detailCross2)
