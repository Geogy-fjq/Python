"""
通过循环打印出如下图案：
输入5:
打印出：
   *
  ***
 *****
具体流程如下：
Step1：外层循环确定行数。
Step2：内层循环确定*的位置和数量。
Step3：打出图案。
"""
m=3
n=5
for i in range(1,m+1):
    for k in range(n-i):
        print("  ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()
