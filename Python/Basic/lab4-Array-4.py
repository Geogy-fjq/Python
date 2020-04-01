"""
请编写一个程序，从键盘读取一个字符串，并确定该字符串是否为回文。
（顺读和倒读都一样的字符串就称为回文。例如：Madam和Anna就是回文字符串。忽视大小写。）
至少准备两组测试数据：
①字符串是回文，例如：madam。
②字符串不是回文，例如：final。
具体流程如下：
Step1：获取字符串，使小写全部转化为大写。
Step2：计算字符串长度，正序读取得到新字符串1和倒序读取得到新字符串2.
Step3：若新字符串1相等于新字符串2，则为回文，否则不是，输出结果。
"""
string=str(input("Please enter your string:"))
string=string.upper()
n=len(string)
a=[]
b=[]
for i in range(n):
    a.append(string[n-1-i])
    b.append(string[i])
if a==b:
    print("Yes.")
else:
    print("No.")
