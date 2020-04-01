c=1
sum=0
while True:
    try:
        a=eval(input("please enter your number:"))
    except:
        print("invalid number please enter again")
        continue
    if a!=0:
        sum=sum+a
        ave=sum/c
        c=c+1
        print("The average number is"+str(ave))
    else:
        break
