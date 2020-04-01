# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 14:24:32 2018

@author: DELL
"""
import pandas as pd
#读取数据
detail1=pd.read_table('Data/Training_Userupdate.csv',sep=',',encoding='gbk')#读取用户信息更新表数据
detail2=pd.read_table('Data/Training_LogInfo.csv',sep=',',encoding='gbk')#读取登录信息表数据
#转换时间字符串
detail1['ListingInfo1']=pd.to_datetime(detail1['ListingInfo1'])
detail1['UserupdateInfo2']=pd.to_datetime(detail1['UserupdateInfo2'])
detail2['Listinginfo1']=pd.to_datetime(detail2['Listinginfo1'])
detail2['LogInfo3']=pd.to_datetime(detail2['LogInfo3'])
print('转换时间字符串后的用户信息更新表对应的时间特征的类型为：\n',detail1[['ListingInfo1','UserupdateInfo2']].dtypes)
print('转换时间字符串后的登录信息表对应的时间特征的类型为：\n',detail2[['Listinginfo1','LogInfo3']].dtypes)

#提取时间信息1(用户信息更新表之ListingInfo1)
year1=[i.year for i in detail1['ListingInfo1']]#提取年份信息
month1=[i.month for i in detail1['ListingInfo1']]#提取月份信息
day1=[i.day for i in detail1['ListingInfo1']]#提取日期信息
week1=[i.week for i in detail1['ListingInfo1']]#提取周信息
weekday1=[i.weekday() for i in detail1['ListingInfo1']]#提取星期信息
weekname1=[i.weekday_name for i in detail1['ListingInfo1']]#提取星期名称信息
print('用户信息更新表中ListingInfo1的前10条年份信息为：',year1[:10])
print('用户信息更新表中ListingInfo1的前10条月份信息为：',month1[:10])
print('用户信息更新表中ListingInfo1的前10条日期信息为：',day1[:10])
print('用户信息更新表中ListingInfo1的前10条周信息为：',week1[:10])
print('用户信息更新表中ListingInfo1的前10条星期信息为：',weekday1[:10])
print('用户信息更新表中ListingInfo1的前10条星期名称信息为：',weekname1[:10])
#提取时间信息2(用户信息更新表之UserupdateInfo2)
year2=[i.year for i in detail1['UserupdateInfo2']]#提取年份信息
month2=[i.month for i in detail1['UserupdateInfo2']]#提取月份信息
day2=[i.day for i in detail1['UserupdateInfo2']]#提取日期信息
week2=[i.week for i in detail1['UserupdateInfo2']]#提取周信息
weekday2=[i.weekday() for i in detail1['UserupdateInfo2']]#提取星期信息
weekname2=[i.weekday_name for i in detail1['UserupdateInfo2']]#提取星期名称信息
print('用户信息更新表中UserupdateInfo2的前10条年份信息为：',year2[:10])
print('用户信息更新表中UserupdateInfo2的前10条月份信息为：',month2[:10])
print('用户信息更新表中UserupdateInfo2的前10条日期信息为：',day2[:10])
print('用户信息更新表中UserupdateInfo2的前10条周信息为：',week2[:10])
print('用户信息更新表中UserupdateInfo2的前10条星期信息为：',weekday2[:10])
print('用户信息更新表中UserupdateInfo2的前10条星期名称信息为：',weekname2[:10])
#提取时间信息3(登录信息表之Listinginfo1)
year3=[i.year for i in detail2['Listinginfo1']]#提取年份信息
month3=[i.month for i in detail2['Listinginfo1']]#提取月份信息
day3=[i.day for i in detail2['Listinginfo1']]#提取日期信息
week3=[i.week for i in detail2['Listinginfo1']]#提取周信息
weekday3=[i.weekday() for i in detail2['Listinginfo1']]#提取星期信息
weekname3=[i.weekday_name for i in detail2['Listinginfo1']]#提取星期名称信息
print('登录信息表中Listinginfo1的前10条年份信息为：',year3[:10])
print('登录信息表中Listinginfo1的前10条月份信息为：',month3[:10])
print('登录信息表中Listinginfo1的前10条日期信息为：',day3[:10])
print('登录信息表中Listinginfo1的前10条周信息为：',week3[:10])
print('登录信息表中Listinginfo1的前10条星期信息为：',weekday3[:10])
print('登录信息表中Listinginfo1的前10条星期名称信息为：',weekname3[:10])
#提取时间信息4(登录信息表之LogInfo3)
year4=[i.year for i in detail2['LogInfo3']]#提取年份信息
month4=[i.month for i in detail2['LogInfo3']]#提取月份信息
day4=[i.day for i in detail2['LogInfo3']]#提取日期信息
week4=[i.week for i in detail2['LogInfo3']]#提取周信息
weekday4=[i.weekday() for i in detail2['LogInfo3']]#提取星期信息
weekname4=[i.weekday_name for i in detail2['LogInfo3']]#提取星期名称信息
print('登录信息表中LogInfo3的前10条年份信息为：',year4[:10])
print('登录信息表中LogInfo3的前10条月份信息为：',month4[:10])
print('登录信息表中LogInfo3的前10条日期信息为：',day4[:10])
print('登录信息表中LogInfo3的前10条周信息为：',week4[:10])
print('登录信息表中LogInfo3的前10条星期信息为：',weekday4[:10])
print('登录信息表中LogInfo3的前10条星期名称信息为：',weekname4[:10])

#计算表中两时间的差(方法一)
time1=detail1['ListingInfo1']-detail1['UserupdateInfo2']#相减
time2=detail2['Listinginfo1']-detail2['LogInfo3']
##计算用户信息更新表中两时间的差
days_1=time1#以日计算
hours_1=time1.dt.total_seconds()/3600#以小时计算
minutes_1=time1.dt.total_seconds()/60#以分钟计算
print('用户信息更新表中两时间的差为（以日计算/days）：\n',days_1)
print('用户信息更新表中两时间的差为（以小时计算/hours）：\n',hours_1)
print('用户信息更新表中两时间的差为（以分钟计算/minutes）：\n',minutes_1)
##计算登录信息表中两时间的差
days_2=time2#以日计算
hours_2=time2.dt.total_seconds()/3600#以小时计算
minutes_2=time2.dt.total_seconds()/60#以分钟计算
print('登录信息表中两时间的差为（以日计算/days）：\n',days_2)
print('登录信息表中两时间的差为（以小时计算/hours）：\n',hours_2)
print('登录信息表中两时间的差为（以分钟计算/minutes）：\n',minutes_2)

''''
#计算用户信息更新表中两时间的差(方法二)
##创建数组，保存全部的计算结果
result1=[]
for i in range(372463):
    time1=pd.datetime(year1[i],month1[i],day1[i]) 
    time2=pd.datetime(year2[i],month2[i],day2[i]) 
    time_1=(time1-time2).days
    result1.append(time_1)
##查看数组中前10个计算结果
print('用户信息更新表中两时间前10条的差为（以日计算/days）：\n')#以日计算
for i in range(10):
    print(result1[i])
print('用户信息更新表中两时间前10条的差为（以小时计算/hours）：\n')#以小时计算
for i in range(10):
    print(result1[i]*24)    
print('用户信息更新表中两时间前10条的差为（以分钟计算/minutes）：\n')#以分钟计算
for i in range(10):
    print(result1[i]*1440) 
   
#计算登录信息表中两时间的差(方法二)
##创建数组，保存全部的计算结果
result2=[]
for i in range(580551):
    time3=pd.datetime(year3[i],month3[i],day3[i]) 
    time4=pd.datetime(year4[i],month4[i],day4[i]) 
    time_2=(time3-time4).days
    result2.append(time_2)
##查看数组中前10个计算结果
print('登录信息表中两时间前10条的差为（以日计算/days）：\n')#以日计算
for i in range(10):
    print(result2[i])
print('登录信息表中两时间前10条的差为（以小时计算/hours）：\n')#以小时计算
for i in range(10):
    print(result2[i]*24)    
print('登录信息表中两时间前10条的差为（以分钟计算/minutes）：\n')#以分钟计算
for i in range(10):
    print(result2[i]*1440)'''





