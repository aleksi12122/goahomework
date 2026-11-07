# 2)

num1 = int(input("Enter a number: "))

if num1 < 2 :
    print("ეს რიცხვი არაა მარტივი")
else :
    is_prime = True
    for i in range (2, (int(num1 ** 0.5)) + 1) :
        if num1 % i == 0 :
            is_prime = False
            break
if is_prime :
    print("ეს რიცხვი მარტივია")
else :
    print("რიცხვი არ არის მარტივი")