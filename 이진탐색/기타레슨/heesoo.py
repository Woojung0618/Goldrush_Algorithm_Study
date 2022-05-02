import sys

n, m = map(int, input().split()) # 강의의 수, 블루레이 개수
n_data = list(map(int, sys.stdin.readline().split()))

start = max(n_data)
end = sum(n_data)

res = 10**9
while(start <= end):
    mid = (start + end) // 2
    count = 1
    tmp = 0

    for i in range(n):
        if (tmp + n_data[i] <= mid): # 만약 현재 블루레이에 비디오를 더 넣을 수 있다면
            tmp += n_data[i]
        else:
            count += 1
            tmp = n_data[i]
        if(count > m):
            break
    if(count > m):
        start = mid + 1
    else:
        end = mid - 1
        if(mid >= start):
            res = min(res, mid)
print(res)
