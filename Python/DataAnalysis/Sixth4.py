# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 18:40:39 2018

@author: DELL
"""
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error,median_absolute_error,explained_variance_score
#实验1处理结果
##读取数据
detail2=pd.read_table('D:/Data/wine_quality.csv',sep=',',encoding='gbk')
##获得wine_quality数据集的数据和标签
data2=np.zeros(shape=(len(detail2),11))
target2=np.zeros(shape=(len(detail2),))
for i in range(len(detail2)):
    s=detail2.iloc[i].str.split(';')
    data2[i]=np.array(s[0][:11])
    target2[i]=np.array(s[0][11])
##将wine_quality数据集分为训练集和测试集:随机选择25%作为测试集，剩余作为训练集
data2_train,data2_test,target2_train,target2_test=train_test_split(data2,target2,test_size=0.25,random_state=45)
##离差标准化
Scaler2=MinMaxScaler().fit(data2_train)#生成规则
data2_train_Scaler=Scaler2.transform(data2_train)#将规则应用于wine_quality训练集
data2_test_Scaler=Scaler2.transform(data2_test)#将规则应用于wine_quality测试集
##降维为8
pca_model2=PCA(n_components=8).fit(data2_train_Scaler)#生成规则
data2_train_Pca=pca_model2.transform(data2_train_Scaler)#将规则应用于wine_quality训练集
data2_test_Pca=pca_model2.transform(data2_test_Scaler)#将规则应用于wine_quality测试集
#构建线性回归模型
##使用训练集训练模型
clf=LinearRegression().fit(data2_train_Pca,target2_train)
print('建立的线性回归模型为:\n',clf)
##使用测试集预测评分
data2_target_pred1=clf.predict(data2_test_Pca)
print('使用测试集预测评分结果为：\n',data2_target_pred1)
#构建梯度提升回归模型
##使用训练集训练模型
GBR=GradientBoostingRegressor().fit(data2_train_Pca,target2_train)
print('建立的梯度提升回归模型为:\n',GBR)
##使用测试集预测评分
data2_target_pred2=GBR.predict(data2_test_Pca)
print('使用测试集预测评分结果为：\n',data2_target_pred2)
#计算均方差、中值绝对误差、可解释方差值
##线性回归模型
print('wine_quality数据线性回归模型的均方差为：',mean_squared_error(target2_test,data2_target_pred1))
print('wine_quality数据线性回归模型的中值绝对误差为：',median_absolute_error(target2_test,data2_target_pred1))
print('wine_quality数据线性回归模型的可解释方差值为：',explained_variance_score(target2_test,data2_target_pred1))
##梯度提升回归模型
print('wine_quality数据梯度提升回归模型的均方差为：',mean_squared_error(target2_test,data2_target_pred2))
print('wine_quality数据梯度提升回归模型的中值绝对误差为：',median_absolute_error(target2_test,data2_target_pred2))
print('wine_quality数据梯度提升回归模型的可解释方差值为：',explained_variance_score(target2_test,data2_target_pred2))
