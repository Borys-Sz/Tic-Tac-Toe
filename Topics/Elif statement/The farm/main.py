money = int(input())
if money < 23:
    print("None")
elif 23 <= money < 46:
    print("1 chicken")
elif 46 <= money < 678:
    chicken = money // 23
    print(str(chicken) + " chickens")
elif 678 <= money < 1296:
    print("1 goat")
elif 1296 <= money < 2592:
    print("1 pig")
elif 2592 <= money < 3848:
    pig = money // 1296
    print(str(pig) + " pigs")
elif 3848 <= money < 6769:
    print("1 cow")
else:   # <= 6769
    sheep = money // 6769
    print(str(sheep) + " sheep")
