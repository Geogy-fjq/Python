"""
使用嵌套循环编写一个小型的猜数字游戏，内重循环要产生一个从1到10的随机数，
可以允许用户猜3次，对每一个数字，显示出来该数字是大、小还是相等，
猜中了或者3次机会用完，提示用户继续还是结束游戏。最后打印输出产生了几次随机数，猜对了几次。
具体流程如下：
Step1：外层循环产生随机数并确定是否继续内循环的条件。
Step2：内层循环判断是否猜对，并确定3次机会。
Step3：提示用户是否继续游戏。
Step4：计算随机数产生和猜对次数。
"""
import random

a = 1
b = 0
c = 0
while a == 1:
    m = random.randint(1, 10)
    b += 1
    i = 0
    while i < 3:
        i += 1
        n = eval(input("Please enter your number:"))
        if n < m:
            print("True number is bigger than yours.")
        elif n > m:
            print("True number is smaller than yours.")
        else:
            print("Right.")
            c += 1
            break
    print("It's over.")
    a = eval(input("To continue please input 1 and to end input  other numbers. "))
print("The time of random number is:", b, ";", "The time of right is:", c)
