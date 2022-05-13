import sys
S = []
print(S)
m = int(input())
for _ in range(m):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == 'add':
        if cmd[1] not in S:
            S.append(cmd[1])
    elif cmd[0] == 'remove':
        if cmd[1] in S:
            S.remove(cmd[1])
    elif cmd[0] == 'check':
        if cmd[1] in S:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'toggle':
        if cmd[1] in S:
            S.remove(cmd[1])
        else:
            S.append(cmd[1])
    elif cmd[0] == 'all':
        S = [i + 1 for i in range(20)]
    else:  # empty
        S = []

