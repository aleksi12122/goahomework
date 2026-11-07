# 3)

number = 434    # ყველა ნებისმიერი რიცხვი შეიძლება აქ

count = 0 
while True :

    num1 = int(input("Enter a number: "))

    if num1 > number :
        print("Your number is higher than correct")
        count += 1
    elif num1 < number :
        print("Your number is lower than correct")
        count += 1
    else :
        print("Your number is correct. You guessed it")
        count += 1
    if number == num1 :
        print(number)
        print("You guessed correct. You won!")
        print("You guessed in - ", count, "attempts")

