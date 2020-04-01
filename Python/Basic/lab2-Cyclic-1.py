"""
设计一个程序，从键盘输入5个整数的累加和并将计算结果输出到屏幕上。
并修改程序设计，询问用户进行多少个整数的累加和。
基本流程如下：
Step1：使用循环结构输入5个整数。
Step2：使用选择结构排除其它输入，确保输入的是整数。
Step3：求和并输出结果。
"""
c = 0
sum = 0
while c < 5:
    try:
        num = int(input("Please enter your integer."))
        c += 1
        sum += num
    except:
        print("Invalid number.Please enter again.")
print("Sum is:", sum)
