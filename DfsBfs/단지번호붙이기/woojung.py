# BFS 풀이
from collections import deque

# 상하좌우
# dx[i], dy[i] 일 때 상(i=0) 하(i=1) 좌(i=2) 우(i=3)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    # print('graph', graph)
    # print('a,b', a, b)
    n = len(graph)
    queue = deque()  # 방문 점 기록
    queue.append((a, b))  # 방문한 점을 순서대로 저장하는 리스트에 해당 점 추가
    graph[a][b] = 0  # 그래프(행렬)에서 해당 점 방문했다는 표시
    count = 1

    # 전체를 돌면서 1인 부분을 탐색
    while queue:  # 방문 점이 존재할 때 아래 반복문 수행
        x, y = queue.popleft()  # 첫번째 방문 점 빼냄
        for i in range(4):  # i=0,1,2,3 (상하좌우)
            nx = x + dx[i]  # nx, ny = 다음 점 위치
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: # 행렬 프레임 밖으로 넘어가는 경우
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0  # 탐색한 지점 0으로 변경하여 다시 방문하지 않도록 함
                queue.append((nx, ny))  # 1이면 방문 점이니까 큐에 추가
                count += 1  # 마을 수 갱신
    return count  # 더이상 방문 점이 없으면 count 리턴
    
n = int(input())
graph = []  # 입력 데이터를 넣어놓는 그래프(행렬) 생성
for i in range(n):
    graph.append(list(map(int, input())))

cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])


# DFS 풀이
n = int(input())
graph = []  # 입력받은 행렬
answer = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def DFS(x, y):  # 재귀 이용
    # (x,y) 점이 1인지 T/F 반환
    if x < 0 or x >= n or y < 0 or y >= n:  # 프레임 밖으로 나가는 경우
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0  # 행렬에 방문했다는 표시
        for i in range(4):  # 상하좌우로 다음 점 위치 지정
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False

count = 0
for i in range(n):
    for j in range(n):
        if DFS(i, j) == True:  # 한 단지 돌고 나왔을 때
            answer.append(count)  # count = 단지에 속한 집 수
            count = 0  # 다음 단지를 위해 0으로 초기화

answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])
