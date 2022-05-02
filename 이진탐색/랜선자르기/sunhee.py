import sys
k,n=map(int,sys.stdin.readline().split())

a=[0]*k
for i in range(k):
    a[i]=int(input())

lt=1
rt=max(a)

res=0
while lt<=rt:
    mid=(lt+rt)//2
    cnt=0
    for i in a:
        cnt+=(i//mid)
    if cnt>=n:
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)
