# 6)

num1 = int(input("Please enter a number: "))

full = 2
much = 0

for i in range(1, num1 + 2) :
    if full > num1:
        break
    full += 2
    much += 1

print(full)
print(much)

#----------------------------------------------------------------

num1 = int(input("Please enter a number: "))

m1 = 2
m2 = 0

while num1 <= m2:
    print(m1)
    m1 += num1

