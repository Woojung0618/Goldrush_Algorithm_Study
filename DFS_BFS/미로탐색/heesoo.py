# 기본 미로 배열 -> maze, 방문 확인 배열 -> visited
# 주변 노드 확인해서 문제 해결!
# 좌표가 경로를 벗어나지 않을 때, 방문여부 확인하고 길이가 0이 아닌지 확인
# 위 조건이 맞다면, 방문여부를 수정하고 큐에 넣는다
# 방문 여부를 확인할 때 몇번째 인지를 적기
import sys

n, m = map(int, sys.stdin.readline().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

maze = [sys.stdin.readline().rstrip() for _ in range(n)]
visited = [[0] * m for _ in range(n)]

queue = [(0,0)]
visited[0][0] = 1

while queue:
    x, y = queue.pop(0)

    if x == n-1 and y == m-1:
        print(visited[x][y])
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and  0 <= ny < m:
            if visited[nx][ny] == 0 and maze[nx][ny] == '1':
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
