# 탑을 다 검사하면 시간 초과 
# 오른쪽에 위치한 탑이 현재 탑의 위치보다 높은 것을 필요없는 탑
# 6 9 5 7 4에서 만약 현재 탑의 위치가 7이면 6의 정보는 필요없다

# 따라서 오른쪽으로 이동하면서 하나씩 탑을 볼 때 
# 자신이 수신될 수 있는 탑의 위치를 찾을 때 이전의 탑의 높이가
# 현재 탑의 높이보다 작으면 버림! 

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
