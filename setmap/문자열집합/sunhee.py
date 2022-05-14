import sys

n,m=map(int, sys.stdin.readline().split())

slist=set()
for _ in range(n):
    slist.add(sys.stdin.readline())

cnt=0

for _ in range(m):
    strm=sys.stdin.readline()
    if strm in slist:
        cnt+=1
print(cnt)
