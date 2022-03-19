# 답은 맞지만 시간 초과
n = int(input())
ball = []
for i in range(n):
    c,s = map(int, input().split())
    ball.append([i, c, s])

ball.sort(key = lambda x: (x[2], x[1]), reverse=True)

A = [0] * n
for b in ball:
    answer = 0
    color_filter = list(filter(lambda x: x[1] != b[1], ball))
    size_filter = list(filter(lambda x: x[2] < b[2], color_filter))
    for i in size_filter:
        answer += i[2]
    A[b[0]] = answer

for a in A:
    print(a)