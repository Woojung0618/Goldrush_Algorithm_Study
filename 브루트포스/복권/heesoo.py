# 확률 = 우리가 구해야 할 경우의 수 / 전체 경우의 수
# 복권에 당첨될 확률 = m개 중에서 k개 뽑을 경우의 수 / n개 중에서 m개 고르는 경우의 수
# 이때, 적어도 k개 이므로 k, k+1, ..., m개 뽑을 경우의 수를 다 더해줘야 한다.
# 그리고 m개 중 k개를 제외한 나머지 수를 뽑아야 하기 때문에 n-mCm-k를 곱한다!!

from itertools import combinations

n, m, k = map(int, input().split())
list_n = [i for i in range(1, n + 1)]
list_m = [g for g in range(1, m + 1)]
list_minus = [l for l in range(1, n - m + 1)]

res_n = len(list(combinations(list_n, m)))
percent = 0

while(m >= k):
    plus = len(list(combinations(list_m, k))) * len(list(combinations(list_minus, m-k)))

    percent += plus / res_n
    k += 1



print(round(percent, 16))
