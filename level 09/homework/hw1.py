

# 1) მომხმარებელს შეაყვანინეთ ასაკი. თუ ასაკი 0-ზე ნაკლებია, გამოიტანეთ "Invalid age". თუ ასაკი 18 ან მეტია, გამოიტანეთ "Adult", 
# სხვა შემთხვევაში — "Minor".



user_age = int(input("Enter your age: "))

if user_age < 0 :
    print("invalid age")
elif user_age >= 18 :
    print("Adult")
else :
    print("Minor")

