from collections import deque
import sys

def DFS(v):
    check[v]=1
    print(v,end=' ')
    for i in range(1,n+1):
        if graph[v][i]==1 and check[i]==0:
            DFS(i)

def BFS(v):
    Q=deque()
    Q.append(v)
    check2[v]=1
    while Q:
        v=Q.popleft()
        print(v,end=' ')
        for i in range(1,n+1):
            if graph[v][i]==1 and check2[i]==0:
                Q.append(i)
                check2[i]=1     #??



n,m,v=map(int,sys.stdin.readline().split())
graph=[[0] * (n + 1) for _ in range(n + 1)] 
check=[0]*(n+1)
check2=[0]*(n+1)


for _ in range(m):
  a, b=map(int, sys.stdin.readline().split())
  graph[a][b]=graph[b][a]=1 #양방향

DFS(v)
print()
BFS(v)