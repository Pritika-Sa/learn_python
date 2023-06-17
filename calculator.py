def addition(a,b):
    sum = a + b
    print(sum)

def subtraction(a,b):
    diff = a - b
    return(diff)

def multiply(a,b):
    product = a * b
    print(product)

def division(a,b):
    div = a / b
    return(div)


print(" Your options are....")
print("1.Addition")
print("2.Subtraction")
print("3.Multiply")
print("4.Division")

choice = int(input("enter your choice : "))
num1 = int(input())
num2 = int(input())

if(choice == 1):
    addition(num1, num2)

elif(choice == 2):
    print(subtraction(num1, num2))

elif(choice == 3):
    multiply(num1, num2)

else:
    print(division(num1, num2))
