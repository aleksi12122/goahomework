# 1)

num1 = int(input("Please enter a number: "))

sum = 0

for i in range(1, num1 + 1) :
    if i % 3 == 0 :
        sum += 1
        
print(sum)


