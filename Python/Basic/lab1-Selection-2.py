"""
根据用户输入的应征税收入计算所得税，下表给出了相关数据，确保程序中包含错误检查部分以防用户输入负数。
应征税收入	所得税
起始	截止
0	50000	0以上的5%
50000	100000	2500+50000以上的7%
100000	……	6000+100000以上的9%
基本流程如下：
Step1：请求输入收入。
Step2：排除收入小于0的情况。
Step3：使用选择结构对收入分类计算并输出结果。
"""
income = eval(input("Please enter your income."))
while income < 0:
    income = eval(input("Invalid income please enter again."))
if 0 <= income <= 50000:
    print("tax=", income * 0.05)
elif 50000 < income <= 100000:
    print("tax=", 2500 + (income - 50000) * 0.07)
elif income > 100000:
    print("tax=", 6000 + (income - 100000) * 0.09)
