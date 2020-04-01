"""
用程序实现两个字符串的比较、追加、拷贝。
具体流程如下：
Step1：输入两个字符串。
Step2：使用选择语句比较，使用简单符号计算追加、拷贝。
Step3：输出结果。
"""
str1=str(input("str1 is:"))
str2=str(input("str2 is:"))
if str1<str2:
    print("str1<str2")
elif str1>str2:
    print("str1>str2")
else:
    print("str1=str2")
str1+=str2
print(str1)
str1=str2
print(str1)
