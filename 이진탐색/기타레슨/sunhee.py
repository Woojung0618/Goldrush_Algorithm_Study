import sys

n,m=map(int,sys.stdin.readline().split())
a=list(map(int,sys.stdin.readline().split()))

lt=1
rt=sum(a)
minm=2147000000
while lt<=rt:
    mid=(lt+rt)//2
    cnt=1
    sum=0
    for i in a:
        if sum+i<=mid:  #현재까지 용량에 새로운 강의 길이를 더했을 때 기준 용량을 넘으면 안됨
            sum+=i
        else:
            cnt+=1
            sum=i
    if mid>=max(a) and mid<minm and cnt<=m:
        minm=mid
        rt=mid-1
    else:
        lt=mid+1
print(minm)
