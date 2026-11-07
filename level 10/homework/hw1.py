# 1)

possitive = 0 
negative = 0 
zero = 0
even = 0
odd = 0

for i in range (10) :
    num1 = int(input("Please enter a number: "))

    if num1 > 0 :
        possitive += 1
        print("This number is possitive")
    elif num1 < 0 :
        negative  += 1
        print("This number is negative")
    else :
        zero += 1
        print("This number is zero")

    if num1 % 2 == 0 :
        even += 1
        print("This number is even")
    else :
        odd += 1
        print("This number is odd")

print("possitive was - ",possitive, "times")
print("negative was - ", negative, "times")
print("zero was - ", zero, "times")
print("even was - ", even, "times")
print("odd was - ",odd, "times")

