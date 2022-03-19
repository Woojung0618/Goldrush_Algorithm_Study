#시간초과

import sys

n=int(sys.stdin.readline())
blist=[]
sizesum=[0]*n
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    blist.append((b,a,i))
blist.sort(reverse=True)

k=0
while k<n:
    size=blist[k][0]
    color=blist[k][1]
    idx=blist[k][2]
    for b,a,i in blist[k:]:
        if b<size and color!=a:
            sizesum[idx]+=b
    k+=1

for i in sizesum:
    print(i)