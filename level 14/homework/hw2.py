# 2)

def calculator(num1, num2, operation) :
    if operation == "+" :
        return num1 + num2
    elif operation == "-" :
        return num1 - num2
    elif operation == "*" :
        return num1 * num2
    else :
        return num1 / num2


print(calculator(123,12, "+"))
print(calculator(43, 76, "-"))
print(calculator(3434, 455, "*"))
print(calculator(10072, 100, "/"))


