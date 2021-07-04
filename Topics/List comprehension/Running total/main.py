first_list = list(str(input()))
second_list = [int(x) for x in first_list]
number = 0
running_total = []
for x in second_list:
    number += x
    running_total.append(number)
print(running_total)