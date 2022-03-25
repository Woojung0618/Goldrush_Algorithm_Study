n = int(input())
towers = list(map(int, input().split()))
answer = []
stack = []

for i in range(n):
    while len(stack) != 0:
        if stack[-1][1] > towers[i]:
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if len(stack) == 0:
        answer.append(0)
    stack.append([i, towers[i]])

for a in answer:
    print(a, end=" ")