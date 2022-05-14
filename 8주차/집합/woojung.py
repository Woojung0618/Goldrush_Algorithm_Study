import sys

S = set()
n = int(sys.stdin.readline())
for _ in range(n):
    m = sys.stdin.readline().split()

    if len(m) == 1:
        if m[0] == 'all':
            S = set([i for i in range(1,21)])
        elif m[0] == 'empty':
            S = set()
    else:
        a, b = m[0], int(m[1])
        if a == 'add':
            S.add(b)
        elif a == 'remove':
            S.discard(b)
        elif a == 'check':
            if b in S: 
                print(1)
            else: 
                print(0)
        elif a == 'toggle':
            if b in S:
                S.discard(b)
            else:
                S.add(b)