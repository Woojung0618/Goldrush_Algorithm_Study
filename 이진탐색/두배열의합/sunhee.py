import imp
import sys
from bisect import bisect

t=int(sys.stdin.readline())
n=int(sys.stdin.readline())
Alist=list(map(int,sys.stdin.readline()))
m=int(sys.stdin.readline())
Blist=list(map(int,sys.stdin.readline()))

Asum=[]
Bsum=[]
for i in range(n):
    sum=0
    for j in range(i, n):
        sum+=Alist[j]
        Asum.append(sum)

for i in range(m):
    sum=0
    for j in range(i, m):
        sum+=Blist[j]
        Bsum.append(sum)

#bisect_left(literable, value) : 왼쪽 인덱스를 구하기
#bisect_right(literable, value) : 오른쪽 인덱스를 구하기

res = 0
Bsum.sort() #bisect이용을 위해서
for sum_a in Asum:
    temp = t - sum_a
    left = bisect.bisect_left(Bsum, temp)
    right = bisect.bisect_right(Bsum, temp)
    res += right-left
print(res)
