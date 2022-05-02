# S 개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값을 구하는 프로그램
# 화면에 있는 이모티콘을 클립보드에 저장
# 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기
# 화면에 있는 이모티콘 중 하나를 삭제
from collections import deque

s = int(input())
d = [[-1] * (s+1) for _ in range(s+1)]

queue = deque()
# 화면 이모티콘 개수, 클럽보드 이모티콘 개수
queue.append((1, 0))
d[1][0] = 0

while queue:
    display, board = queue.popleft()
    if d[display][display] == -1:
        d[display][display] = d[display][board] + 1
        queue.append((display, display))
    if display + board <= s and d[display + board][board] == -1:
        d[display + board][board] = d[display][board] + 1
        queue.append((display + board, board))

answer = -1
for i in range(s + 1):
    if d[s][i] != -1:
            if answer == -1 or answer > d[s][i]:
                answer = d[s][i]
print(answer)
    

