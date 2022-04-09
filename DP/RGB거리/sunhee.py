#26 40 83   1번째 줄은 저장만하고
#49 60 57   빨간색을 고르면 앞줄에 파,초 중에 더 저렴한 거 암거나 고르면 됨
#           그러면 두번째 줄은 빨간색을 고른거니까 그 칸에다 현재까지 비용 저장
#13 89 99   마찬가지로 3번쨰 줄에서 빨간색을 고르면 앞줄에서 파,초 중에 고르면됨
#n번째 줄 입장에서 n-1번째 줄을 본인 색깔과 다른 색을 선택해주면 안 겹침

import sys

n = int(sys.stdin.readline())
cost =[list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
    cost[i][0] += min(cost[i-1][1], cost[i-1][2])
    cost[i][1] += min(cost[i-1][0], cost[i-1][2])
    cost[i][2] += min(cost[i-1][0], cost[i-1][1])

print(min(cost[-1]))     