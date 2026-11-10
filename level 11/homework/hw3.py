# 3)

mixed_list = ["aleqsi", 12, 765, True, 0.543, "bread", False, 654, 15.65, 143.654, "saba"]

i = 0
while i < 5 :
    mixed_list[i], mixed_list[10 - i] = mixed_list[10 - i], mixed_list[i]
    i += 1

print(mixed_list)


