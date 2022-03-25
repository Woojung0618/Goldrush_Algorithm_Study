# 1 ~ 6번째 줄
# 1 ~ P번째까지 나눠져 있음

# 각 줄에 대해 스택 사용


import sys

n, p = map(int, sys.stdin.readline().split())
data = [[0] for _ in range(1, 7)]
result = 0

for i in range(n):
    line, number =  map(int, sys.stdin.readline().split())
    # 스택이 비어 있다면
    if data[line] == 0:
        data[line].append(number)
        result += 1
    # 스택이 비어있지 않다면
    else:
        # 프렛의 번호가 같은 줄에 있는 것보다 작을 때
        while data[line] and number < data[line][-1]:
            data[line].pop()
            result += 1

        # 프렛의 번호가 같은 줄에 있는 것보다 클 때
        if data[line] != 0 or number > data[line][-1]:
            data[line].append(p)
            result += 1

        # 프렛의 번호가 같을 때
        else: 
            pass # 단순히 실행할 코드가 없다는 뜻!!

print(result)