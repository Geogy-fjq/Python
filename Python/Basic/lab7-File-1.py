"""
设计一个程序，保存客户文件。文件记录了客户姓名，
用户输入姓之后，程序能够搜索文件，并输出所有该姓氏的客户姓名。
具体流程如下：
Step1：通过嵌套循环输入每个学生所有成绩并计算平均分。
Step2：通过嵌套循环输入每门课程所有学生的成绩并计算平均分。
Step3：输出结果。
"""
a = 0
c = 0
name = open("name.txt", "w")
while a == 0:
    try:
        b = str(input("Please enter the name."))
        name.write(b + "\n")
        a = eval(input("Continue to enter 0 and end to enter other numbers."))
    except:
        break

n = str(input("Please enter the first name:"))
name = open("name.txt", "r")
for line in name.readlines():
    line = line.strip()
    A = line.split(" ")
    if A[0] == n:
        print(line)
