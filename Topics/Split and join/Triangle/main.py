n = int(input())
h = "#"
for i in range(1, n + n, 2):
    h = "#" * i
    print(h.center(n + n))