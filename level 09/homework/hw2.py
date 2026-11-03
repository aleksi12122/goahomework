
# 2) მომხმარებელს შეაყვანინეთ რიცხვი. თუ რიცხვი დადებითია და ლუწია, გამოიტანეთ "Positive Even". თუ დადებითია და 
# კენტია, გამოიტანეთ "Positive Odd". თუ უარყოფითია, გამოიტანეთ "Negative", სხვა შემთხვევაში — "Zero".



user_number = int(input("Enter a number: "))

if user_number > 0 and user_number % 2 == 0 :
    print("Positive Even")
elif user_number > 0 and user_number % 2 != 0 :
    print("Possitive Odd")
elif user_number < 0 :
    print("Negative")
else :
    print("zero")

