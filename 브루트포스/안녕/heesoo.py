# 주어진 체력내에서 기쁨느낌, i번째 사람 -> L[i] 체력잃고 J[i]만큼의 기쁨 얻음
# 최대 기쁨을 출력하는 프로그램 

# 0,1 배낭문제 알고리즘으로 이전 최대치와 이전 값을 빼고 현재 값을 넣은 것과 비교하여 더 가치가 높은 것을 넣어주자!
# https://dreamtreeits.tistory.com/m/56
from sys import stdin

N = int(stdin.readline())
L = [0] + list(map(int, stdin.readline().split()))
J = [0] + list(map(int, stdin.readline().split()))

dp = [[0] * 101 for _ in range(N + 1)]

for i in range(1, N+1):
    for j in range(1, 101):
        if L[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]]+J[i])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][99])