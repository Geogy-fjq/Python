"""
设计一个程序，输入一组正数，存储到数组中，求出这组数的平均值并输出结果。
程序使用不同模块，分别完成计算平均值、输出结果。
基本流程如下：
Step1：输入一组正数存于数组中。
Step2：使用不同模块计算平均值、输出结果。
"""
c = []
i = 0
j = 0
while i == 0:
    n = int(input("Please enter your positive number:"))
    if n > 0:
        c.append(n)
        j += 1
        i = int(input("Continue to enter 0 and end to enter other numbers."))
    else:
        print("Invalid number.Please enter again.")
        continue


def average():
    S = 0
    for a in range(j):
        S += c[a]
        average = S / j
    return average


def result():
    result = average()
    print("The average is:", result)


result()
