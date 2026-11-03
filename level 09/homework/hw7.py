# 7)

start = int(input("Enter a first number: "))
end = int(input("Enter a last number: "))

while start <= end :
    if start > 0 and start % 2 == 0 :
        print("Positive Even")
    else :
        print(start)
    start += 1

