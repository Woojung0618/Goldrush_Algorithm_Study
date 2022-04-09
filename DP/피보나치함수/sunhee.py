#재귀함수 이용시 시간초과
#f(2)= f(1) 1번, f(0) 1번
#f(3)= f(2) 1번, f(1) 1번  ->  f(1) 2번, f(0) 1번 
# ...
#f(n)에서 0 count는   (n-1)과 (n-2)의 0의 개수 합
#1도 마찬가지

import sys

def fibonacci(n):
    zerocount = [1,0]
    onecount = [0,1]
    if n <= 1:
        return
    for i in range(2, n+1):
        zerocount.append(zerocount[i-1] + zerocount[i-2])
        onecount.append(onecount[i-1] + onecount[i-2])
 
    return zerocount, onecount
 
n = int(sys.stdin.readline())
zerocount, onecount = fibonacci(40)
 
for _ in range(n):
    m = int(sys.stdin.readline())
    print("%d %d" % (zerocount[m], onecount[m]))
    
