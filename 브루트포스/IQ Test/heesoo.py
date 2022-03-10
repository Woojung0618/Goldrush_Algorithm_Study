# N의 경우를 나누기
# N = 1) 규칙을 찾을 수 X -> A출력
# N = 2) 숫자가 같은 경우 -> 그 숫자, 숫자가 다른 경우 -> A출력
# N >= 3) a, b를 구해야함 y = ax + b 이므로
# ex) 3개 이상의 숫자 n1, n2, n3 -> n2 = a*n1 + b, n3 = a*n2 + b
#     따라서 a = (n3 - n2) / (n2 - n1), b = n2 - a*n1
# 0으로 나누면 런타임에러 발생 -> 예외처리 해줘야함
import sys

n = int(sys.stdin.readline())
item = list(map(int, sys.stdin.readline().split()))

if n == 1:
    print("A")
elif n == 2:
    if item[0] == item[1]:
        print(item[1])
    else:
        print("A")
else:
    if (item[1] - item[0]) == 0:
        a = 0
    else:
        a = (item[2] - item[1]) // (item[1] - item[0])
    b = item[1] - a*item[0]
    
    for i in range(n-1):
        result = a*item[i] + b
        if item[i + 1] != result:
            print("B")
            exit() #프로그램 종료
    print(a*item[-1] + b)
