# 3)

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

if num1 < num2 :
    small = num1
else :
    small = num2

for i in range (small, 0, - 1) :
    if num1 % i == 0 and num2 % 2 == 0 :
        answer = i
        break
print(i)
