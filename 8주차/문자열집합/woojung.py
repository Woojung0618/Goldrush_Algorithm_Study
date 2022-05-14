import sys
n, m = map(int, input().split())
S = set([])
ans = 0
for _ in range(n):
    S.add(sys.stdin.readline().rstrip())
for _ in range(m):
    c = sys.stdin.readline().rstrip()
    if c in S:
        ans += 1
print(ans)

# answer = 0
# for c in C:
#     if c in S:
#         answer += 1
# print(answer)