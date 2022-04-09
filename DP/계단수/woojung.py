# ** dp에 이용되는 숫자의 특징은 2가지다. DP[마지막 자리의 숫자][BITMASKING]
# 참고 블로그 : https://rccode.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-1562%EB%B2%88-%EA%B3%84%EB%8B%A8-%EC%88%98

# 0~9 모두 사용했는지 확인 -> 비트 마스크
# ex.  2, 4, 5 를 가짐 -> 0000110100(2) -> 52
# ex. 모두 가짐 -> 1111111111(2) 


MOD = 1000000000
MAX = (1<<10)-1  # 2^10 -1 = 1023

n = int(input())
dp = [[0] * (MAX+1) for _ in range(10)]  # dp[마지막 자리의 숫자(0~9)][BITMASKING(0~MAX-1)]

for i in range(1, 10):
    dp[i][1<<i] = 1  # 각 자리수마다 비트마스크 초기값 1로 설정

for _ in range(2, n+1):
    next_dp = [[0] * (MAX+1) for _ in range(10)]

    for i in range(10):
        for j in range(MAX+1):  # 비트마스크
            if i > 0:
                next_dp[i][j | (1 << i)] = (next_dp[i][j | (1 << i)] + dp[i-1][j]) % MOD
            if i < 9:
                next_dp[i][j | (1 << i)] = (next_dp[i][j | (1 << i)] + dp[i+1][j]) % MOD
        dp = next_dp

print(sum(dp[i][MAX] for i in range(10)) % MOD)
