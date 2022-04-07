import sys

def DFS(x,y):
    global cnt
    cnt+=1
    board[x][y]='0'
    for i in range(4):
        x2=x+dx[i]
        y2=y+dy[i]
        if 0<=x2<n and 0<=y2<n and board[x2][y2]=='1':
            DFS(x2,y2)
            


n=int(sys.stdin.readline())
board=[]
for i in range(n):
    board.append(list(sys.stdin.readline().strip()))
dx=[-1,0,1,0]
dy=[0,1,0,-1]
res=[]
for i in range(n):
    for j in range(n):
        if board[i][j]=='1':  #단지 처음 발견
            cnt=0
            DFS(i,j)
            res.append(cnt)
res.sort()    
print(len(res))
for i in res:
    print(i)
