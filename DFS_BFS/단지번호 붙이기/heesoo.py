import sys

n = int(sys.stdin.readline())
matrix = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]

for i in range(n):
    line = sys.stdin.readline().strip()
    # enumerate() 함수는 기본적으로 인덱스와 원소로 이루어진 tuple을 만들어줌
    # j -> 인덱스 번호, k -> 값 
    for j, k in enumerate(line):
        matrix[i][j] = int(k)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, c):
    visited[x][y] = 1 # 방문표시
    global number # 아파트 단지 수
    if matrix[x][y] == 1:
        number += 1
    
    # 이 위치에서 상단좌우 살핀 후, 좌표를 확인해서 dfs 적용
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                dfs(nx, ny, c)

# 아파트 단지를 세기 위한 변수
count = 1
numberlist = []
number = 0

for a in range(n):
    for b in range(n):
        if matrix[a][b] == 1 and visited[a][b] == 0:
            dfs(a, b, count)
            numberlist.append(number)
            number = 0

print(len(numberlist))
for n in sorted(numberlist):
    print(n)

