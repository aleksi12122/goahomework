
# 1)

user_age = int(input("Enter your age: "))

if user_age > 0 and user_age <= 12 :
   print("ბავშვი")
elif user_age > 12 and user_age <= 18 :
   print("მოზარდი")
elif user_age > 18 and user_age <= 60 :
   print("სრულწლოვანი")
elif user_age > 60 and user_age <= 100 :
   print("მოხუცი")

else :
   print("არასწორი პასუხი")



