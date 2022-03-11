n = int(input())
loss = list(map(int, input().split()))
pleasure = list(map(int, input().split()))
dp = [[0] * 101 for _ in range(n+1)]

for i in range(n):
    for j in range(101):
        if loss[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-loss[i]] + pleasure[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n-1][99])