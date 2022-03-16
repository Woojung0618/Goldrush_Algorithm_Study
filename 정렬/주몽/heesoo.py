# 고유 번호 정렬한 후, 
# 양끝 값에서 시작해서 둘의 합이 m보다 작으면 왼쪽 값을 작게 만들고 크면 오른쪽 값을 작게 만들어야한다.

# 투포인터 알고리즘
# -> 리스트에 순차적으로 접근해야 할 때, 두 개의 점의 위치를 기록하면서 처리하는 알고리즘 
# -> 시작점과 끝점 2개로 접근할 데이터의 범위를 표현할 수 있다.
# ex. 특정한 합을 가지는 부분 연속 수열 찾기


import sys

n = int(input())
m = int(input())
numbers = list(map(int, sys.stdin.readline().split()))

numbers.sort()
count = 0

i = 0
j = len(numbers) - 1

while (i < j):
    if numbers[i] + numbers[j] > m:
        j -= 1
    elif numbers[i] + numbers[j] < m:
        i += 1
    else:
        count += 1
        i += 1
        j -= 1

print(count)

# 시간초과 코드
'''
n = int(input())
m = int(input())
number = list(map(int, sys.stdin.readline().split()))
count = 0

for i in range(0, len(number)-1):
    for j in range(i+1, len(number)):
        if(m == number[i] + number[j]):
            count += 1

print(count)
'''