# 2)

count = int(input("Enter your item count: "))
full = 0

for i in range (count) :
    full += int(input("Enter item costs: "))

if full > 200 :
    full = full * 0.85
elif full >= 100 and full < 200 :
    full = full * .90

print("you have to pay - ", full, "lari")

