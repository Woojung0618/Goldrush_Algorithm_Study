n = int(input())
p = []

for i in range(n):
    p.append(list(map(int, input().split())))

# 0, 1, 2 -> 빨, 초, 파
for i in range(1, len(p)):
    # i번째 집을 빨강으로 칠했을 때 최솟값
    p[i][0] = min(p[i-1][1], p[i-1][2]) + p[i][0]
    # i번째 집을 초록으로 칠했을 때 최솟값
    p[i][1] = min(p[i-1][0], p[i-1][2]) + p[i][1]
    # i번째 집을 파랑으로 칠했을 때 최솟값
    p[i][2] = min(p[i-1][0], p[i-1][1]) + p[i][2]
# 세개 값 중에서 가장 작은 값을 출력
print(min(p[n-1][0], p[n-1][1], p[n-1][2]))