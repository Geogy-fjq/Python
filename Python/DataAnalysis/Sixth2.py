# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 18:40:23 2018

@author: DELL
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.metrics import fowlkes_mallows_score
from sklearn.metrics import silhouette_score
from sklearn.metrics import calinski_harabaz_score
#实验1处理结果
##读取wine数据
detail1=pd.read_table('D:/Data/wine.csv',sep=',',encoding='gbk')
##获得wine数据集的数据和标签
data1=detail1.iloc[:,1:].values
target1=detail1.iloc[:,0].values
##标准化wine数据集
Scaler1=MinMaxScaler().fit(data1)
data1_Scaler=Scaler1.transform(data1)
##降维为8
pca_model1=PCA(n_components=8).fit(data1_Scaler)
data1_Pca=pca_model1.transform(data1_Scaler)
#构建聚类数目为3的K-Means模型
kmeans=KMeans(n_clusters=3,random_state=150).fit(data1_Pca)#构建并训练模型
print('构建的K-Means模型为：\n',kmeans)
#求取FMI
for i in range(2,11):
    #构建并训练模型
    kmeans=KMeans(n_clusters=i,random_state=150).fit(data1_Pca)
    score=fowlkes_mallows_score(target1,kmeans.labels_)
    print('wine数据聚%d类FMI评价分值为：%f'%(i,score))
#取模型的轮廓系数，绘制轮廓系数折线图
silhouettteScore=[]
for i in range(2,11):
    #构建并训练模型
    kmeans=KMeans(n_clusters=i,random_state=150).fit(data1_Pca)
    score=silhouette_score(data1,kmeans.labels_)
    silhouettteScore.append(score)
plt.figure(figsize=(10,6))#创建画布
plt.plot (range(2,11),silhouettteScore)#绘制折线图
plt.xticks(range(2,11))#设置x轴刻度
plt.title('轮廓系数折线图')#添加标题
plt.xlabel('聚类数目')#添加x轴名称
plt.ylabel('轮廓系数')#添加y轴名称
plt.savefig('轮廓系数折线图.png')
plt.show()
#求取Calinski-Harabasz指数
for i in range(2,11):
    #构建并训练模型
    kmeans=KMeans(n_clusters=i,random_state=150).fit(data1_Pca)
    score=calinski_harabaz_score(data1,kmeans.labels_)
    print('wine数据聚%d类Calinski-Harabasz指数为：%f'%(i,score))