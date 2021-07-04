n = int(input())
lis = []
for x in range(n):
    a = input().split(" ")
    if a[1] == "win":
        lis.append(a[0])
print(lis)
print(len(lis))