"""
输入某年某月某日，判断这一天是这一年的第几天？如：2000年3月 1日就是2000年的第61天31+29+1从１计数）
基本流程如下：
Step1：请求输入年月日。
Step2：通过除4无余确定是否闰年，确定二月份天数，数组记录每个月份天数。
Step3：计算天数并输出结果。
"""
year = eval(input("Please enter the year."))
month = eval(input("Please enter the month."))
day = eval(input("Please enter the day."))
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
i = 0
Days = 0
if year % 4 == 0 and year % 100 != 0:
    day[2] = 29
while i < month:
    Days = Days + days[i]
    i += 1
print("It is the", Days + day, "day of the", year, "year")
