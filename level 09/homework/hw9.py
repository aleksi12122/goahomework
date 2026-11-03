# 9)

n = int(input("Enter a number: "))
x = 1

while x <= n :
    if x % 2 == 0 and x % 3 == 0 :
        print("Special Number")
    elif x % 2 == 0 :
       print("Even")
    elif x % 3 == 0 :
        print("Divisible by 3")
    else :
        print(x)
    
    x += 1
