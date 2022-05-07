import sys
n,k=map(int,sys.stdin.readline().split())

stack=[i for i in range(1,n+1)]
result=[]
while len(stack)>0:
    for i in range(k):
        if i==k-1:
            result.append(stack.pop(0))
        else:
            stack.append(stack.pop(0))

print('<',end='')
print(*result, sep=', ',end='')
print('>')
