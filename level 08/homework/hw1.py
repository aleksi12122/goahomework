
# 1)

num1 = int(input("Please, enter a whole number: "))

cycle = 0

while cycle < num1  :
  print(cycle)
  cycle += 1

if cycle % 2 == 0 :
    print(cycle,"- This Number Is Even")

else :
    print(cycle,"- This Number Is Odd")




# 2)


num2 = int(input("Please, enter a whole number: "))
x = 0

while x < num2 :
    print(x)
    x += 1

if x % 5 == 0 :
    print(x)
    print("This number is diviseble by 5")
else :
    print("This number:")
    print(num2)




# 3)

correct_password = "Aleksi2011"       # python123

user_password = input("Please, enter your password : ")

while user_password != correct_password :
    print("Wrong Password! ")
    user_password = input("Please, enter your password : ")

if user_password == correct_password  :
    print("Correct Password. Acces Granted! ")

else :
    print("Wrong Password! ")




# 4)

num3 = int(input("Please, enter a whole number: "))

for i in range(1, num3 + 1) :
    print(i)

if i % 2 == 0 :
    print("This number is even:")
    print(i)
else :
    print("This number is odd:")
    print(i)




# 5)

num4 = int(input("Please, enter a whole number: "))

for cycle in range(1, num4 + 1) :
    print(cycle)

if cycle % 3 == 0 :
    print("This number:", cycle)

else:
    print("This number is not diviseble by 3")
