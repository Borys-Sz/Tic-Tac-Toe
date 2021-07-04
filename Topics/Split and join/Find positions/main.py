a = input().split()
b = input()
c = []
for idx, item in enumerate(a):
    if item == b:
        c.append(idx)
if len(c) == 0:
    print("not found")
else:
    for idx in c:
        print(idx, end=" ")