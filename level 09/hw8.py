# 8)

user_age = int(input("Enter your age: "))
user_test_score = int(input("Enter your test score: "))

if user_age >= 18 and user_test_score >= 70 :
    print("You passed!")
    
elif user_age < 18 and user_test_score >= 70 :
    print("Good result, but you are under 18!")

elif user_test_score < 70 and user_age < 18 :
    print("You failed and you are underage!")

