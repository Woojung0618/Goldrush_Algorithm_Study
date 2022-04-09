# fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

zero = [1, 0, 1]
one = [0, 1, 1]

def fibonacci(num):
    length = len(zero)
    # 배열의 길이를 구해서 배열의 길이보다 입력받은 숫자가 크면 반복문 시작
    # 그렇지 않으면 저장되어 있는 값 출력
    if num >= length:
        for i in range(length, num+1):
            zero.apppend(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print('{} {}'.format(zero[num], one[num]))

T = int(input())

for _ in range(T):
    fibonacci(int(input()))