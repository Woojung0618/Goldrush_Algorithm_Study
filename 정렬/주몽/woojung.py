# 정렬 해놓고 투 포인터로 풀어야 시간초과 안나고 풀리는 문제
n = int(input())
m = int(input())
list = list(map(int, input().split()))
list.sort()
answer = 0
i, j = 0, n-1
while i < j:
    if list[i] + list[j] == m:
        answer += 1
        i += 1
        j -= 1
    elif list[i] + list[j] < m:
        i += 1
    else:
        j -= 1
print(answer)