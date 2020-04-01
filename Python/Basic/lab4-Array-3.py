"""
两个具有相同行数和列数的矩阵可以相乘得出第三个矩阵。假设有如下两个矩阵：
　　　　　　       A 　　　　B
矩阵A和B的乘积是第三个矩阵C，其大小为n*n, C的每个元素由下面等式给定：
　　　　　　　　　　Cij=ΣAikBkj　　
编写一个程序先读取A和B的元素，再计算矩阵C。
① A、B两个数组的值在程序中通过初始化方式得到。
② A、B两个数组的值通过输入函数得到，并检查结果是否正确。
具体流程如下：
Step1:定义matrix函数和矩阵A、B、C。
Step2:使用循环结构获取矩阵A、B。
Step3:相乘算法得到矩阵C，并输出结果。
"""
import numpy
A=[]
B=[]
C=[]
n=eval(input("Please enter the side:"))
for r in range(1,n+1):
    D=[]
    for c in range(1,n+1):
        print("The element of row",r,"colum",c,"in A is:")
        a=eval(input())
    A.append(D)
A=numpy.matrix(A)
for r in range(1,n+1):
    D=[]
    for c in range(1,n+1):
        print("The element of row",r,"colum",c,"in B is:")
        a=eval(input())
    B.append(D)
B=numpy.matrix(B)
C=A*B
print(C)
