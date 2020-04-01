"""
求两个数的最大公约数，这两个数通过输入函数输入。
基本流程如下：
Step1：通过函数输入两个数。
Step2：两数比较大小，取较小数。
Step3：通过循环结构自上而下使两数除以某数余数为零得出最大公约数。
"""


def num():
    a = eval(input("Number1 is:"))
    b = eval(input("Number2 is:"))
    return a, b


def diviser():
    a, b = num()
    if a != 0 and b != 0:
        if a <= b:
            c = a
        else:
            c = b
        for i in range(c + 1, 1, -1):
            if a % i == 0 and b % i == 0:
                print("Diviser is:", i)
                return i
                break
            else:
                continue
    else:
        print("No diviser.")


diviser()
