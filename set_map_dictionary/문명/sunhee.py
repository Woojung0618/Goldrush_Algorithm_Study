import sys

n,k=map(int,sys.stdin.readline().split())
dx=(0,0,-1,1)
dy=(-1,1,0,0)

mapk=[[0] * n for _ in range(n)]

for _ in range(k):
    x,y=map(int,sys.stdin.readline().split())
    x=x-1
    y=y-1
    mapk[x][y]=1

mapcnt=0
cnt=0
while True:
    cnt+=1
    if mapcnt==n*n:
        break
    for i in range(n):
        for j in range(n):
            if mapk[i][j]>=1:
                mapcnt+=1

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<n:
            mapk[nx][ny]=1

print(cnt)