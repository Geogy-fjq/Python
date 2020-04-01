"""
设计一个程序，对学生总成绩进行排名。假设有5名学生成绩，
包括姓名和3门课的成绩，计算每个学生课程成绩总分，并按照总分成绩由高到低排名。
基本流程如下：
Step1：按顺序分别输入姓名和成绩并保存于数组中。
Step2：计算每个同学的总成绩并进行排名。
Step3：按照成绩排名，对应顺序输出姓名。
"""
import numpy
l1=[]
l2=[]
l3=[]
sum=0
for j in range(1,6):
    sum=0
    print("Please enter the name of student",j,":")
    A=input()
    l1.append(A)
    for i in range(1,4):
        print("Please enter the score of subject",i,"of student",j,":")
        a=eval(input())
        sum+=a
    l2.append(sum)
for j in range(1,6):
    m=max(l2)
    b=l2.index(m)
    c=l1[b]
    del l1[b]
    del l2[b]
    print(c,"",m)
