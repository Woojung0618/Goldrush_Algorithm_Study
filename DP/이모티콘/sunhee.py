from collections import deque

S = int(input())

queue = deque([[1, 0, 0]])  # 화면의 이모티콘 개수, 클립보드 이모티콘 개수, 연산 횟수

check = [[False] * 1001 for _ in range(1001)]   #시간 단축을 위해 방문한 횟수면 더 이상 방문하지 않도록 체크
check[1][0] = True

while queue:

    screen, clipboard, cnt = queue.popleft()

    if screen == S:  # 만약 스크린의 개수와 S가 동일하다면
        print(cnt)  # 걸린 횟수를 출력
        break  

    for i in range(3):  # 연산을 3번 수행한다.

        # 화면에 있는 이모티콘을 복사해서 클립보드에 저장
        if i == 0:
            new_clipboard, new_screen = screen, screen

        # 화면에 클립보드에 있는 이모티콘 들을 추가
        elif i == 1:
            new_screen, new_clipboard = screen + clipboard, clipboard
            
        # 화면에 있는 이모티콘 개수 한개 빼기
        else:
            new_screen, new_clipboard = screen - 1, clipboard

        # 범위를 벗어나거나 이미 방문한 적이 있다면 넘어가
        if new_screen >= 1001 or new_screen < 0 or new_clipboard >= 1001 or new_clipboard < 0 or check[new_screen][
            new_clipboard]:
            continue

        # 방문처리 후 연산 횟수를 +1
        check[new_screen][new_clipboard] = True
        queue.append([new_screen, new_clipboard, cnt + 1])