# 3)

correct_password = "python123"

user_password = input("Please enter your password: ")


while user_password != correct_password:
    print("Wrong")
    user_password = input("Please enter your password: ")


print("Acces Granted!")


