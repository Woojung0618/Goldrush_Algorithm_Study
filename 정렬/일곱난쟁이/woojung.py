list = [int(input()) for _ in range(9)]
list.sort()
list_sum = sum(list)

for i in range(9):
    for j in range(i+1, 9):
        if list_sum - (list[i] + list[j]) == 100:
            p1 = list[i]
            p2 = list[j]
            # list.remove(list[i])
            # list.remove(list[j])

list.remove(p1)
list.remove(p2)
for i in list:
    print(i)

