# 5)

total = 0
count = 0
positive_count = 0

print("Enter a numbers. if you enter - 0 program(code) will end")

while True :
    number = int(input("Enter a number: "))

    if number == 0 :
        break
    count += 1
    total += number

    if number > 0 :
        sign = "positive"
        positive_count += 1

    else :
        sigh = "negative"

    pair = "even" if number % 2 == 0 else "odd"


print("numbers")
print("number count - ", total)
print("total number - ", count)
print("positive number - ",positive_count)

