# 크기가 작고 색이 다른 공을 사로잡자-> 그 공의 크기만큼 점수를 얻음
# 크기를 기준으로 오름차순 정리 하고
# 현재까지의 모든 공의 크기 합에서 색깔이 같거나 크기가 같은 공의 무게를 빼준다.

# 중복제거를 하는 이유?


import sys

n = int(input())

data = []

total = 0
weight = set()


for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    data.append((a, b))
    total += b
    weight.add(b)
weight = sorted(weight)

res = [0] * (len(weight) + 1)

total_pf = [0] * (len(weight) + 1)


j = 0
for i in range(n):
    while sort_data[i][1] < sort_data[j][0]:
        weights[]