n = int(input())
li = []
for i in range(n):
    x = int(input())
    li.append(x)

suma = float(sum(li))
mean = suma / n
print(mean)