# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 18:40:00 2018

@author: DELL
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
#读取数据
detail1=pd.read_table('Data/wine.csv',sep=',',encoding='gbk')
detail2=pd.read_table('Data/wine_quality.csv',sep=',',encoding='gbk')
#拆分数据和标签
##获得wine数据集的数据和标签
data1=detail1.iloc[:,1:].values
print('wine的数据为：\n',data1)
target1=detail1.iloc[:,0].values
print('wine的标签为：\n',target1)
##获得wine_quality数据集的数据和标签
data2=np.zeros(shape=(len(detail2),11))
target2=np.zeros(shape=(len(detail2),))
for i in range(len(detail2)):
    s=detail2.iloc[i].str.split(';')
    data2[i]=np.array(s[0][:11])
    target2[i]=np.array(s[0][11])
print('wine_quality的数据为：\n',data2)
print('wine_quality的标签为：\n',target2)
#将wine_quality数据集分为训练集和测试集
data2_train,data2_test,target2_train,target2_test=train_test_split(data2,target2,test_size=0.25,random_state=45)#随机选择25%作为测试集，剩余作为训练集
print('wine_quality原始数据的形状为：',data2.shape)
print('wine_quality原始标签的形状为：',target2.shape)
print('wine_quality训练集数据的形状为：',data2_train.shape)
print('wine_quality训练集标签的形状为：',target2_train.shape)
print('wine_quality测试集数据的形状为：',data2_test.shape)
print('wine_quality测试集标签的形状为：',target2_test.shape)
#离差标准化wine和wine_quality数据集
Scaler1=MinMaxScaler().fit(data1)#生成wine的规则
Scaler2=MinMaxScaler().fit(data2)#生成wine_quality的规则
data1_Scaler=Scaler1.transform(data1)#将规则应用于wine数据集
data2_Scaler=Scaler2.transform(data2)#将规则应用于wine_quality数据集
print('离差标准化前wine数据集的最小值为：',np.min(data1))
print('离差标准化后wine数据集的最小值为：',np.min(data1_Scaler))
print('离差标准化前wine数据集的最大值为：',np.max(data1))
print('离差标准化后wine数据集的最大值为：',np.max(data1_Scaler))
print('离差标准化前wine_quality数据集的最小值为：',np.min(data2))
print('离差标准化后wine_quality数据集的最小值为：',np.min(data2_Scaler))
print('离差标准化前wine_quality数据集的最大值为：',np.max(data2))
print('离差标准化后wine_quality数据集的最大值为：',np.max(data2_Scaler))
#对wine和wine_quality数据集进行PCA降维
pca_model1=PCA(n_components=8).fit(data1_Scaler)#生成wine的规则
pca_model2=PCA(n_components=8).fit(data2_Scaler)#生成wine_quality的规则
data1_Pca=pca_model1.transform(data1_Scaler)#将规则应用于wine数据集
data2_Pca=pca_model2.transform(data2_Scaler)#将规则应用于wine_quality数据集
print('PCA降维前wine数据集的形状为：',data1_Scaler.shape)
print('PCA降维后wine数据集的形状为：',data1_Pca.shape)
print('PCA降维前wine_quality数据集的形状为：',data2_Scaler.shape)
print('PCA降维后wine_quality数据集的形状为：',data2_Pca.shape)











