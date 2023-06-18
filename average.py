def avg(a,b,c,d,e):
    average = (a+b+c+d+e)/5
    return average
flag = True
while(flag):
    print("The given options are:-")
    print("1.Calculate te options")
    print("2.Exit")

    choice = int(input())

    if (choice == 1):
        num1 = int(input("enter mark1 :"))
        num2 = int(input("enter mark2 :"))
        num3 = int(input("enter mark3 :"))
        num4 = int(input("enter mark4 :"))
        num5 = int(input("enter mark5 :"))
        print(avg(num1,num2,num3,num4,num5))
    elif(choice == 2):
        flag = False
    else:
        print("invalid choice")



