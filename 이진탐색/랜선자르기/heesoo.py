import sys

# 오영식이 이미 가지고 있는 랜선의 개수, 필요한 랜선의 개수
k, n = map(int, input().split())
data = [int(sys.stdin.readline()) for _ in range(k)] # 이미 가지고 있는 각 랜선의 길이

start, end = 1, max(data) # 랜선 최소길이, 가장 긴 길이

while (start <= end): # 이분탐색이 완료될 때까지 반복
    mid = (start + end) // 2 # 이분탐색 중간값 
    lines = 0
    for i in data:
        lines += i // mid # 랜선을 자른 수
    
    # 랜선을 자른 수가 만들어야 될 랜선의 수보다 큰 경우
    if lines >= n:
        start = mid + 1 # 랜선의 최소 길이를 중간값보다 1크게 설정
    # 랜선을 자른 수가 만들어야 될 랜선의 수보다 작은 경우
    else:
        end = mid - 1 # 랜선의 최대 길이를 중간값보다 1작게 설정
print(end) # end는 결과값