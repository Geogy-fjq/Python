# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 17:18:51 2018

@author: DELL
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']='SimHei'#设置中文显示
plt.rcParams['axes.unicode_minus']=False
data_load=np.load('Data/populations.npz')#读取人口数据
print(data_load.keys())#获取值（辅助性步骤，查看数据）
name=data_load['feature_names']#提取feature_names数组，作为数据标签
data=data_load['data']#提取data数组，作为数据
print(name)#（辅助性步骤，查看数据）
print(data)#（辅助性步骤，查看数据）
p1=plt.figure(figsize=(12,14))#创建画布
#子图1:散点图
ax1=p1.add_subplot(2,1,1)#创建2行1列子图，并开始第1幅
plt.scatter(data[:20,0],data[range(19,-1,-1),1],marker='o',c='k')#绘制年末总人口散点图
plt.scatter(data[:20,0],data[range(19,-1,-1),2],marker='s',c='b')#绘制男性人口散点图
plt.scatter(data[:20,0],data[range(19,-1,-1),3],marker='*',c='r')#绘制女性人口散点图
plt.scatter(data[:20,0],data[range(19,-1,-1),4],marker='^',c='g')#绘制城镇人口散点图
plt.scatter(data[:20,0],data[range(19,-1,-1),5],marker='x',c='y')#绘制乡村人口散点图
plt.title('1996~2015年人口数据特征散点图')#添加标题
plt.xlabel('年份')#添加x轴名称
plt.ylabel('人口数（万人）')#添加y轴名称
plt.xticks(range(20),data[range(19,-1,-1),0])#设置x轴刻度
plt.legend(['年末总人口','男性人口','女性人口','城镇人口','乡村人口'])#添加图例
plt.savefig('散点图和折线图.png')
#子图2：折线图
ax2=p1.add_subplot(2,1,2)#创建2行1列子图，并开始第2幅
plt.plot(data[:20,0],data[range(19,-1,-1),1],'k-')#绘制年末总人口折线图
plt.plot(data[:20,0],data[range(19,-1,-1),2],'b-.')#绘制男性人口折线图
plt.plot(data[:20,0],data[range(19,-1,-1),3],'r-.')#绘制女性人口折线图
plt.plot(data[:20,0],data[range(19,-1,-1),4],'g--')#绘制城镇人口折线图
plt.plot(data[:20,0],data[range(19,-1,-1),5],'y--')#绘制乡村人口折线图
plt.title('1996~2015年人口数据特征折线图')#添加标题
plt.xlabel('年份')#添加x轴名称
plt.ylabel('人口数（万人）')#添加y轴名称
plt.xticks(range(20),data[range(19,-1,-1),0])#设置x轴刻度
plt.legend(['年末总人口','男性人口','女性人口','城镇人口','乡村人口'])#添加图例
plt.savefig('散点图和折线图.png')
plt.show()

