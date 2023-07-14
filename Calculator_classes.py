class calculator:
    def addition(self,a, b):
        sum = a + b
        print(sum)
    def subtraction(self,a, b):
        diff = a - b
        print(diff)
    def multiplication(self,a, b):
        multiply = a * b
        print(multiply)
    def division(self,a, b):
        div = a / b
        print(div)
c = calculator()

print("The options are:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

options = int(input("enter your choice :"))
num1= int(input("a :"))
num2= int(input("b :"))

if(options == 1):
    c.addition(num1, num2)

elif(options == 2):
    c.subtraction(num1, num2)

elif(options == 3):
    c.multiplication(num1, num2)

else:
    c.division(num1, num2)

