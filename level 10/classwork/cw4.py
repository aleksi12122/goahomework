# 4)

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))


while num2 != 0 :
    remainder = num1 % num2 
    num1 = num2
    num2 = remainder

print(str(num1))