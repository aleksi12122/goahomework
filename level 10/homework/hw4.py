# 4)

for i in range (5) :
    names = input("Enter student name: ")
    scores = int(input("Now enter his score: "))

    if scores >= 90 :
        print("შესანიშნავი")
    elif scores >= 70 and scores < 90 :
        print("კარგი")
    elif scores >= 50 and scores < 70 :
        print("დამაკმაყოფილებელი")
    elif scores < 50 :
        print("ჩაჭრილი")
    else :
        print("არასწორი ქულა")
        
    print(names)
    print(scores)

