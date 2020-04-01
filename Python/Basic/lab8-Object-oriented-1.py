"""
设计一个程序，由用户输入雇员的工时数及每小时的工资，程序采用面向对象的方法，
输出雇员的总工资，并且可以处理任意数量的雇员信息。
具体流程如下：
Step1：编写面向对象流程。
Step2：输入雇员的工时数及每小时的工资，计算总工资并输出。
"""
class Employee:
    'The working hours of every employees and the salary of every employees.'
    def _init_(self,name,Salary):
        self.name=name
        self.Salary=Salary
    def Input(self):
        name=str(input("The name is:"))
        hours=eval(input("The hours is:"))
        salary=eval(input("The everyhours salary is:"))
    def Count(self):
        Salary=salary*hours
    def Output(self):
        print("Name:",self.name,"Salary:",self.Salary)
n=0
while n==0:
    try:
        name=str(input("The name is:"))
        hours=eval(input("The hours is:"))
        salary=eval(input("The everyhours salary is:"))
        Salary=salary*hours
        print("Name:",name,"Salary:",Salary)
        n=eval(input("Continue to enter 0 and end to enter other numbers."))
    except:
        break
