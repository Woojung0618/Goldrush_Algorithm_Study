import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
stack_list = []
check = [0]*n

for i in range(n):
    d = data[i]
    while stack_list and data[stack_list[-1]] < d:
        stack_list.pop()
    if stack_list:
        check[i] = stack_list[-1] + 1
    stack_list.append(i)

print(' '.join(list(map(str, check))))
