from collections import deque
import sys

n,m=map(int,sys.stdin.readline().split())
maze=[]
for i in range(n):
    maze.append(list(sys.stdin.readline().strip()))
dis=[[0]*m for _ in range(n)]   #몇칸 왔나 표시
dx=[-1,0,1,0]
dy=[0,1,0,-1]
Q=deque()   #내가 들릴 위치
Q.append((0,0))
maze[0][0]=1
while Q:
    tmp=Q.popleft()
    for i in range(4):
        x=tmp[0]+dx[i]
        y=tmp[1]+dy[i]
        if 0<=x<n and 0<=y<m and maze[x][y]=='1':
            maze[x][y]='0'
            dis[x][y]=dis[tmp[0]][tmp[1]]+1
            Q.append((x,y))

print(dis[n-1][m-1]+1)