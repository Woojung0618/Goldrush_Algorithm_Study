import sys

h_list=[]
for _ in range(9):
    h_list.append(int(sys.stdin.readline()))

h_list.sort()
h_sum=sum(h_list)
h_break=False
for i in range(9):
    for j in range(i+1,9):
        if h_sum-(h_list[i]+h_list[j])==100:
            h_list.pop(i)
            h_list.pop(j-1)
            h_break=True
            break
    if h_break==True:
        break

for i in h_list:
    print(i)



