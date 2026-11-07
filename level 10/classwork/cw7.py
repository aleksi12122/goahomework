# 7)

n = int(input("Enter a number: "))

while n < 0 :
    n = int(input("Enter a number: "))


reverse_num = 0
while n > 0 :
    numbers = n % 10
    reverse_num = reverse_num * 10 + numbers
    n = n // 10

print(reverse_num)


