import sys
input = sys.stdin.readline

K = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))


sum_A = []
for i in range(N):
    sum = 0
    for j in range(i, N):
        sum += A[j]
        sum_A.append(sum)

sum_B = []
for i in range(M):
    sum = 0
    for j in range(i, M):
        sum += B[j]
        sum_B.append(sum)

result = 0
sum_B.sort()
for sum_a in sum_A:
    temp = K - sum_a

print(result)