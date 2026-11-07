# 6)

num1 = int(input("Enter a  number: "))

full = 0 
while num1 > 0 :
    digit = num1 % 10
    if digit % 2 == 1 :
        full += digit
    num1 //= 10

print(full)