# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 20:48:06 2018

@author: DELL
"""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']='SimHei'#设置中文显示
plt.rcParams['axes.unicode_minus']=False
data_load=np.load('Data/populations.npz')#读取人口数据
name=data_load['feature_names']#提取feature_names数组，作为数据标签
data=data_load['data']#提取data数组，作为数据

#创建画布1:绘制直方图
p1=plt.figure(figsize=(12,12))
label1=data[range(19,-1,-1),0]#定义直方图的标签
#画布1之子图1:男女人口数目条形图
ax1=p1.add_subplot(2,1,1)#创建2行1列子图，并开始第1幅
plt.bar(np.arange(20)-0.15,data[range(19,-1,-1),2],width=0.3)#绘制男性人口数目条形图
plt.bar(np.arange(20)+0.15,data[range(19,-1,-1),3],width=0.3)#绘制女性人口数目条形图
plt.title('1996~2015年男女人口数目条形图')#添加标题
plt.xlabel('年份')
plt.ylabel('人口数（万人）')
plt.xticks(range(20),label1)
plt.legend(['男性人口','女性人口'])#添加图例
plt.savefig('条形图.png')
#画布1之子图2:城乡人口数目条形图
ax2=p1.add_subplot(2,1,2)#创建2行1列子图，并开始第2幅
plt.bar(np.arange(20)-0.15,data[range(19,-1,-1),4],width=0.3)#绘制城镇人口数目条形图
plt.bar(np.arange(20)+0.15,data[range(19,-1,-1),5],width=0.3)#绘制乡村人口数目条形图
plt.title('1996~2015年城乡人口数目条形图')#添加标题
plt.xlabel('年份')
plt.ylabel('人口数（万人）')
plt.xticks(range(20),label1)
plt.legend(['城镇人口','乡村人口'])#添加图例
plt.savefig('条形图.png')
plt.show()

#创建画布2：绘制饼图
p2=plt.figure(figsize=(15,10))
label3=['男性人口','女性人口']#定义男女人口数目饼图的标签
label4=['城镇人口','乡村人口']#定义城乡人口数目饼图的标签
explode=[0.01,0.01]#定义各项距离圆心n个半径
#子图1:1996年男女人口数目饼图
ax1=p2.add_subplot(2,3,1)#创建2行3列子图，并开始第1幅
plt.pie(data[19,(2,3)],explode=explode,labels=label3,autopct='%1.1f%%')#绘制1996年男女人口数目饼图
plt.title('1996年男女人口数目饼图')#添加标题
plt.savefig('饼图.png')
#子图2:2010年男女人口数目饼图
ax2=p2.add_subplot(2,3,2)#创建2行3列子图，并开始第2幅
plt.pie(data[5,(2,3)],explode=explode,labels=label3,autopct='%1.1f%%')#绘制2010年男女人口数目饼图
plt.title('2010年男女人口数目饼图')#添加标题
plt.savefig('饼图.png')
#子图3:2015年男女人口数目饼图
ax3=p2.add_subplot(2,3,3)#创建2行3列子图，并开始第3幅
plt.pie(data[0,(2,3)],explode=explode,labels=label3,autopct='%1.1f%%')#绘制2015年男女人口数目饼图
plt.title('2015年男女人口数目饼图')#添加标题
plt.savefig('饼图.png')
#子图4:1996年城乡人口数目饼图
ax4=p2.add_subplot(2,3,4)#创建2行3列子图，并开始第4幅
plt.pie(data[19,(4,5)],explode=explode,labels=label4,autopct='%1.1f%%')#绘制1996年城乡人口数目饼图
plt.title('1996年城乡人口数目饼图')#添加标题
plt.savefig('饼图.png')
#子图5:2010年城乡人口数目饼图
ax5=p2.add_subplot(2,3,5)#创建2行3列子图，并开始第5幅
plt.pie(data[5,(4,5)],explode=explode,labels=label4,autopct='%1.1f%%')#绘制2010年城乡人口数目饼图
plt.title('2010年城乡人口数目饼图')#添加标题
plt.savefig('饼图.png')
#子图6:2015年城乡人口数目饼图
ax6=p2.add_subplot(2,3,6)#创建2行3列子图，并开始第6幅
plt.pie(data[0,(4,5)],explode=explode,labels=label4,autopct='%1.1f%%')#绘制2015年城乡人口数目饼图
plt.title('2015年城乡人口数目饼图')#添加标题
plt.savefig('饼图.png')
plt.show()

#创建画布3:绘制箱线图
p1=plt.figure(figsize=(10,10))
label5=['男性人口','女性人口']#定义男女人口数目箱线图的标签
label6=['城镇人口','乡村人口']#定义城乡人口数目箱线图的标签
#画布3之子图1:男女人口数目箱线图
ax1=p1.add_subplot(2,1,1)#创建2行1列子图，并开始第1幅
gdp=(list(data[range(19,-1,-1),2]),list(data[range(19,-1,-1),3]))
plt.boxplot(gdp,notch=True,labels=label5,meanline=True)#绘制男女人口数目箱线图
plt.title('1996~2015年男女人口数目箱线图')#添加标题
plt.ylabel('人口数（万人）')
plt.savefig('箱线图.png')
#画布3之子图2:城乡人口数目箱线图
ax2=p1.add_subplot(2,1,2)#创建2行1列子图，并开始第2幅
gdp=(list(data[range(19,-1,-1),4]),list(data[range(19,-1,-1),5]))
plt.boxplot(gdp,notch=True,labels=label6,meanline=True)#绘制城乡人口数目箱线图
plt.title('1996~2015年城乡人口数目箱线图')#添加标题
plt.ylabel('人口数（万人）')
plt.savefig('箱线图.png')
plt.show()
