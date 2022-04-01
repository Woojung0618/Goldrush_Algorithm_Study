n = int(input())

for i in range(n):
    line = list(input().split(' '))
    stack = []
    for l in line:
        stack.append(l)
    print('Case #%i: ' %(i+1), end='')
    while stack:
        print(stack.pop(), end=' ')