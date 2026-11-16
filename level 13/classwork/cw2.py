# 2)


name = "aLEqsi DaneLIA"

print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.find("q"))

city = "PaRiS"

print(city.upper())
print(city.lower())
print(city.capitalize())
print(city.find("P"))


#დამატებითი მეთოდი 1: .replace()
# ცვლის ქვესტრინგის ყველა შემთხვევას ახალით და აბრუნებს ახალ სტრინგს.
# ორიგინალი სტრინგი უცვლელი რჩება.


conversation = "cat is very good cat"
print(conversation.replace("cat", "dog"))       # გამოიტანს: dog is very good dog
print(conversation.replace("good", "pretty", 1))



# დამატებითი მეთოდი 2: .strip()

# შლის თეთრ სივრცეებს (space, tab, newline) სტრინგის დასაწყისიდან და ბოლოდან.
# .lstrip() მხოლოდ მარცხნიდან, .rstrip() მხოლოდ მარჯვნიდან შლის.

conversation = "hello"
print(conversation.strip())             # გამოიტანს: "hello"

gmail = "  user@example.com\n"
print(gmail.strip())              # გამოიტანს: "user@example.com"


# დამატებითი მეთოდი 3: .split()

# სტრინგს ყოფს ნაწილებად გამყოფის მიხედვით და აბრუნებს სიას (list).
# თუ გამყოფი არ არის მითითებული, გამოიყენება ნებისმიერი თეთრი სივრცე.

convers = "i love python"
print(convers.split())        # გამოიტანს: ['i', 'love', 'python']

date = "2026-11-14"
print(date.split("-"))

