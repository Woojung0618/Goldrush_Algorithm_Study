# 화면의 이모티콘 s, 클립보드의 이모티콘 c

# 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
# 복사 : (s,c) -> (s,s)
# 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
# 붙여넣기 : (s,s) -> (s+c, c)
# 3. 화면에 있는 이모티콘 중 하나를 삭제한다.
# (s,c) -> (s-1, c)

# => 모든 연산은 1초가 걸리니 모든 경로의 가중치는 1이다.
# 따라서, dist[s][c] + 1 과 같이 1을 더해줘야 한다.

from collections import deque
n = int(input())
emoji = [[-1] * (n+1) for _ in range(n+1)]
emoji[1][0] = 0

def bfs(n):
    q = deque()
    q.append((1, 0))
    while q:
        s, c = q.popleft()
        if emoji[s][s] == -1:  # -1이면 아직 처리 X. 근데 왜 [s][s] 지?
            emoji[s][s] = emoji[s][c] + 1  # 하나도 처리 안된 상태면 1번 과정 수행
            q.append((s, s))
        if s+c <= n and emoji[s+c][c] == -1:  # 1번은 수행되고 2번은 수행 안된 상태일 때
            q.append((s+c, c))
            emoji[s+c][c] = emoji[s][c] + 1  # 2번 과정 수행
        if s-1 >= 0 and emoji[s-1][c] == -1:  # 2번은 수행되고 3번은 수행 안된 상태일 때
            q.append((s-1, c))
            emoji[s-1][c] = emoji[s][c] + 1  # 3번 과정 수행


bfs(n)
answer = -1
for i in range(n+1):
    if emoji[n][i] != -1:
        if answer == -1 or answer > emoji[n][i]:
            answer = emoji[n][i]

print(answer)