from collections import deque

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = graph[v2][v1] = 1  # 두 점이 연결되어있다는 의미로 1
# print(graph)

# 리스트를 써서 pop(0)하게 되면 시간복잡도가 O(N)이다.
# 그래서 시간복잡도가 O(1)인 deque를 사용한다.
def bfs(v):
    queue = deque()
    queue.append(v)
    visit_bfs[v] = 1

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in range(1, n+1):  # 다른 점들 탐색
            if visit_bfs[i] == 0 and graph[v][i] == 1:  # 방문하지 않았고, 두 점이 이어져 있으면
                queue.append(i)
                visit_bfs[i] = 1  # 방문했다는 표시

def dfs(v):
    visit_dfs[v] = 1
    print(v, end=" ")
    for i in range(1, n+1):
        if visit_dfs[i] == 0 and graph[v][i] == 1:
            dfs(i)


visit_bfs = [0] * (n+1)
visit_dfs = [0] * (n+1)

dfs(v)
print()
bfs(v)
