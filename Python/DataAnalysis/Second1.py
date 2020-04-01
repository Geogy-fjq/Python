# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 15:16:00 2018

@author: DELL
"""
import numpy as np#导入Numpy库

#创建数组
arr1=np.arange(0,1,0.01).reshape(10,10)#改变数组一的形状，使之与数组二相同
print("第一个数组为：\n",arr1)
arr2=np.random.randn(10,10)
print("随机数组为：\n",arr2)

#对两个数组进行四则运算
print("相加结果为：\n",arr1+arr2)
print("相减结果为：\n",arr1-arr2)
print("相乘结果为：\n",arr1*arr2)
print("相除结果为：\n",arr1/arr2)
print("取幂结果为：\n",arr1**arr2)

#对随机数组进行统计分析
print("重新排序值的下标为：\n",arr2.argsort())#返回重新排序值的下标
arr2.sort(axis=1)#沿着横轴排序
print("沿着横轴排序后的数组为：\n",arr2)
arr2.sort(axis=0)#沿着纵轴排序
print("沿着纵轴排序后的数组为：\n",arr2)
arr2.sort()#直接排序
print("直接排序后的数组为：\n",arr2)

print("按行进行元素重复后的数组为：\n",arr2.repeat(2,axis=0))#按行进行元素重复
print("按列进行元素重复后的数组为：\n",arr2.repeat(2,axis=1))#按列进行元素重复
arr3=np.tile(arr2,2)#对数组进行重复
print("重复后的数组为：\n",arr3)
print("去重后的数组为：\n",np.unique(arr3))#对数组进行去重

print("数组的和为：\n",np.sum(arr2))#计算数组的和
print("数组横轴的和为：\n",arr2.sum(axis=1))#计算数组横轴的和
print("数组纵轴的和为：\n",arr2.sum(axis=0))#计算数组纵轴的和
print("数组的均值为：\n",np.mean(arr2))#计算数组的均值
print("数组的标准差为：\n",np.std(arr2))#计算数组的标准差
print("数组的方差为：\n",np.var(arr2))#计算数组的方差
print("数组的最小值为：\n",np.min(arr2))#计算数组的最小值
print("数组的最大值为：\n",np.max(arr2))#计算数组的最大值
print("数组最小元素的索引为：\n",np.argmin(arr2))#返回数组最小元素的索引
print("数组最大元素的索引为：\n",np.argmax(arr2))#返回数组最大元素的索引
print("数组元素的累计和为：\n",np.cumsum(arr2))#计算数组元素的累计和
print("数组元素的累计积为：\n",np.cumprod(arr2))#计算数组元素的累计积

