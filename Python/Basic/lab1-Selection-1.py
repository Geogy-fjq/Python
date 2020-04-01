"""
熟悉RAPTOR算法设计环境。设计一个程序，输出一个提示信息，请求用户输入一个数字，
如果大于0则输出“Positive”，如果小于0则输出“Negative”，如果等于0则输出“Zero”。
基本流程如下：
Step1：请求输入一个数字。
Step2：判断输入数字的正负性质，对应输出结果。
"""
num = eval(input("Please enter a number."))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
elif num == 0:
    print("Zero")
