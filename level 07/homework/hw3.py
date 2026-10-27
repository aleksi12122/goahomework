# 3)

num1 = int(input("Please enter a number: "))

even_sum = 0

for i in range(0, num1, 2) :
    even_sum += i

print(even_sum)


#-------------------------------------------------

n = int(input("Please enter a number: "))

x = 0
even_sum = 0

while x <= n:
    even_sum += x
    x += 2

print(even_sum)


