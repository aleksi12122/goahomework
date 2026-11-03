# 4)

real_number = 2324

user_number = int(input("Guess the number: "))

while  user_number != real_number :
    print("თქვენი რიცხვი მეტია ჩაფიქრებულზე")
    user_number = int(input("Guess the number: "))

if  user_number < real_number :
    print("თქვენი რიცხვი ნაკლებია ჩაფიქრებულ რიცხვზე")
    user_number = int(input("Guess the number: "))

elif user_number == real_number :
    print("თქვენ წარმატებით გამოიცანით რიცხვი!")

else :
    print("არასწორი რიცხვია!")

