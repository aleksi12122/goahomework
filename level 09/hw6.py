# 6)

correct_password = "python123"

user_password = input("Enter your password: ")

while correct_password != user_password :
    print("wrong password")
    user_password = input("Enter your password: ")

else :
    print("Acces granted")
