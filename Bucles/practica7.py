num1 = 1
num2 = 1
while (num1 <= 10):
    print (num1,"X", num2,"=", num1*num2)
    num2=num2+1
    if (num2==11):
        num2=1
        num1+=1
        print ("--------------")