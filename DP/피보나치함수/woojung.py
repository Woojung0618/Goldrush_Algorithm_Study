# n = 0 : 0을 1번 호출, 1을 0번 호출
# n = 1 : 0을 0번 호출, 1을 1번 호출
# n = 2 : (n=0일 때 호출 값) + (n=1일 때 호출 값)
# n = 3 : (n=1일 때 호출 값) + (n=2일 때 호출 값)
n = int(input())

for _ in range(n):
    m = int(input())
    a0 = [1, 0]  # 0 호출 횟수 기록
    a1 = [0, 1]  # 1 호출 횟수 기록
    for i in range(2, m+1):
        a0.append(a0[i-1] + a0[i-2])
        a1.append(a1[i-1] + a1[i-2])
    print('{0} {1}'.format(a0[m], a1[m]))

############ 시간초과 #########

# def fibo(m):
#     global a0, a1
#     if m == 0:
#         a0 += 1
#     elif m == 1:
#         a1 += 1
#     else:
#         fibo(m-1) + fibo(m-2)
#     return a0, a1

# for _ in range(n):
#     a0, a1 = 0, 0
#     m = int(input())
#     a0, a1 = fibo(m)
#     print('{0} {1}'.format(a0, a1))

