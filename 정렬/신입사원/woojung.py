def solve(n, score1, score2):
    print(score1)
    # 문제가 이해가 안됨.. 첫번째 사례가 왜 4명인지? '5 5' 1명 아닌가

t = int(input())

for _ in range(t):
    score1, score2 = [], []
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        score1.append(a)
        score2.append(b)
        solve(n, score1, score2)
        
    print(score1, score2)