"""
用赋初值的方法将15个数存放在一个数组中，首先对这15个数进行排序；
接着使用输入函数输入一个数，要求用折半查找法找出该数是数组第几个元素的值。如果该数不在数组中，则输出“无此数”。
基本流程如下：
Step1：产生15个随机数。
Step2：将这15个数存于数组中并进行排序。
Step3：使用折半查找找出这个数的位置，不在该数组中则输出“无此数”。
"""
import random

A = []
for i in range(1, 16):
    a = random.randint(0, 100)
    A.append(a)
A = sorted(A)
print(A)
b = eval(input("Please enter your number:"))


def binary_search(A, b):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if b < A[mid]:
            high = mid - 1
        elif b > A[mid]:
            low = mid + 1
        elif b == A[mid]:
            print("The number is the element", mid + 1, ".")
            break
    else:
        print("It's no there.")


binary_search(A, b)
