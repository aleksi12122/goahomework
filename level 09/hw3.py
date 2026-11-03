
# 3) შექმენით ორი ცვლადი: correct_username = "gio" და correct_password = "12345". მომხმარებელს შეაყვანინეთ სახელი და 
# პაროლი. თუ ორივე სწორია, გამოიტანეთ "Login successful!", სხვა შემთხვევაში — "Wrong username or password!". გამოიყენეთ and.


correct_username = "gio"
correct_password = "12345"

user_name = input("Enter your name: ")
user_password = input("Enter yout password: ")

if user_name == correct_username and correct_password == user_password :
    print("Login successful!")
else :
    print("Wrong username or password!")

