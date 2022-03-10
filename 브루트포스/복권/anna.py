
#1359 python
#처음에 조합을 계산하는 함수를 만들어야 하나 싶어서 def Combination까지 만들었는데
#찾아보니 조합을 계산해주는 라이브러리가 있길래 추가해서 사용하였다

from itertools import combinations  #조합을 계산해주는 라이브러리

n, m, k = map(int, input().split())

#n개 중 m개를 선택하는 모든 경우의 수
#combination(n,m)
answer = 0
all = [*combinations([i for i in range(n)], m)]

#m개 중 k개 이상을 포함하는 경우의 수
#적어도 k개의 수가 일치 -> k개 이상의 수가 일치하면 당첨
for i in all:
    count = 0
    for j in range(m):
        if i[j] < m:
            count += 1
    if count >= k:
        answer += 1

#당첨 확률 = 당첨 조합의 수 * 실패 조합의 수 / 선택한 조합의 수
print(answer / len(all))

