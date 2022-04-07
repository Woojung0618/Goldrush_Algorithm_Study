import sys

n=int(sys.stdin.readline())
top=list(map(int,sys.stdin.readline().split()))
maxlentop=[(0,top[0])]
receive=[0]

for i in range(1,n):
    while 1:
        if len(maxlentop)==0:
            maxlentop.append((i,top[i]))
            receive.append(0)
            break
        if maxlentop[-1][1]>=top[i]:
            receive.append(maxlentop[-1][0]+1)
            maxlentop.append((i,top[i]))
            break
        else:
            maxlentop.pop()

for i in receive:
    print(i,end=' ')