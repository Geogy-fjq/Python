# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 16:05:04 2018

@author: DELL
"""
import numpy as np
#创建国际象棋棋盘：黑色为1，白色为0
matr=np.matrix([[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]])#创建8*8初始矩阵
#把1、3、5、7行和0、2、4、6列元素设置为1
matr[(0,2,4,6),:]=1
matr[:,(1,3,5,7)]=1
#把1、3、5、7行和2、4、6、8列交叠处元素设置为0
matr[0,(1,3,5,7)]=0
matr[2,(1,3,5,7)]=0
matr[4,(1,3,5,7)]=0
matr[6,(1,3,5,7)]=0
print("该棋盘为：\n",matr)
