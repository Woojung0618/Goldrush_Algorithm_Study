# dfs, bfs를 구현할 줄 알아야 하는 문제!!
# 인덱스 값과 해당 노드를 맞춰주기 위해서 N+1로 만들었다.
# for문을 통해 입력받은 노드의 번호에 맞게 1로 채워준다!
import sys

n, m, v = map(int, sys.stdin.readline().split())
matrix = [[0] * (n+1) for _ in range(n+1)] # 인덱스 값과 해당 노드를 맞춰주기 위해서

for _ in range(m):
    line = list(map(int, sys.stdin.readline().split()))
    matrix[line[0]][line[1]] = 1
    matrix[line[1]][line[0]] = 1

def bfs(start):
    visited = [start]
    queue = [start]
    while queue:
        n = queue.pop(0)
        for c in range(len(matrix[start])):
            if matrix[n][c] == 1 and (c not in visited):
                visited.append(c)
                queue.append(c)
    return visited

def dfs(start, visited):
    visited += [start]
    for  c in range(len(matrix[start])):
        if matrix[start][c] == 1 and (c not in visited):
            dfs(c, visited)
    return visited

# *를 앞에 붙이면 list안의 결과물들을 출력해줌
print(*dfs(v, []))
print(*bfs(v))


