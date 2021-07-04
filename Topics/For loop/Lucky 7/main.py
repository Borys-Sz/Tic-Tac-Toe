n = int(input())
li = []
for i in range(n):
    x = int(input())
    li.append(x)
for x in li:
    if x % 7 == 0:
        print(x ** 2)
