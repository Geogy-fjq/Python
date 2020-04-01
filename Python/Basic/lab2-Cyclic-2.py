"""
从控制台输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
基本流程如下：
Step1：请求输入一行字符。
Step2：用选择结构将每个字符按性质分类，并用循环结构统计各类个数。
Step3：输出结果。
"""
alp_num=0
spa_num=0
int_num=0
oth_num=0
a=input("Please enter a string.")
for i in a:
    if i.isdigit():
        int_num+=1
    elif i.isalpha():
        alp_num++1
    elif i.isspace():
        spa_num+=1
    else:
        oth_num+=1
print("alp_num is:",alp_num,"；","spa_num is:",spa_num,";","int_num is:",int_num,";","oth_num is:",oth_num)
