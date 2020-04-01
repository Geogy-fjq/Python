"""
设计一个程序，已知一个班级30个学生的英语成绩，
使用一维数组保存该班级学生的英语成绩，并统计60分以上学生的数量且输出统计结果。
具体流程如下：
Step1：创建数组，使用循环结构保存30个同学的成绩。
Step2：循环结构内部使用条件语句统计60分以上学生数量。
Step3：输出结果。
"""
grades = []
standers = 0
for i in range(30):
    num = float(input("Enter the grade:"))
    grades.append(num)
for a in grades:
    if a > 60:
        standers += 1
print("The number of standers is:", standers)
