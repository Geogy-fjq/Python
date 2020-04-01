# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 18:40:31 2018

@author: DELL
"""
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report
#读取wine数据
detail1=pd.read_table('D:/Data/wine.csv',sep=',',encoding='gbk')
#区分数据和标签
data1=detail1.iloc[:,1:].values#数据
target1=detail1.iloc[:,0].values#标签
#将wine数据集分为训练集和测试集
data1_train,data1_test,target1_train,target1_test=train_test_split(data1,target1,test_size=0.25,random_state=45)#随机选择25%作为测试集，剩余作为训练集
#离差标准化wine数据集
Scaler1=MinMaxScaler().fit(data1_train)#生成wine的规则
data1_trainScaler=Scaler1.transform(data1_train)#将规则应用于wine训练集
data1_testScaler=Scaler1.transform(data1_test)#将规则应用于wine测试集
#构建SVM模型
##使用训练集训练模型
svm=SVC().fit(data1_trainScaler,target1_train)
print('建立的SVM模型为：\n',svm)
##预测测试集结果
data1_target_pred=svm.predict(data1_testScaler)
print('预测测试集结果为：\n',data1_target_pred)
#打印分类报告
print('',classification_report(target1_test,data1_target_pred))