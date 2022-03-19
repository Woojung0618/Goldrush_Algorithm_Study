#백준 1940 주몽

N = int(input())
M = int(input())
num = list(map(int, input().split()))
num.sort()
#n과 m을 입력받고, 숫자도 입력받은 후 정렬한다

count = 0

for i in range(N):
    for j in range(N):
        if (num[i] + num[j] == M):  #더한 값이 M과 같으면 숫자 세준다
            count += 1

count = int(count/2)
print(count)