"""
设计一个程序，输出一个提示信息，请求用户输入班级数量及学生数量，
程序使用嵌套循环结构进行学生成绩统计，且需要在屏幕上给出计算结果。
具体流程如下：
Step1：通过嵌套循环输入每个学生所有成绩并计算平均分。
Step2：通过嵌套循环输入每门课程所有学生的成绩并计算平均分。
Step3：输出结果。
"""
N = eval(input("Please enter the number of class."))
n = eval(input("Please enter the number of student."))
for a in range(1, n + 1):
    sum = 0
    for b in range(1, N + 1):
        print("Please enter mark", b, "of student", a, ".")
        c = eval(input())
        sum = sum + c
    average = sum / N
    print("The sum of student", a, "is:", sum, ";", "The average of student", a, "is:", average, ".")
for b in range(1, N + 1):
    sum = 0
    for a in range(1, n + 1):
        print("Please enter mark", b, "of student", a, ".")
        c = eval(input())
        sum = sum + c
    average = sum / n
    print("The average of mark", b, "of all the students is:", average, ".")
