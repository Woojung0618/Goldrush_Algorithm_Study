# 중복되지 않은 원소를 얻고자 할 때, 집합의 성질을 가지고 있는 내장함수인 set을 사용!
import sys

t = int(input()) # 테스트케이스의 개수
for _ in range(t):
    n = int(input()) # 수첩1에 적어 놓은 정수의 개수
    n_data = set(sys.stdin.readline().split()) # 수첩1에 적혀있는 정수들 n개
    m = int(input()) # 수첩2에 적어 놓은 정수의 개수
    m_data = list(sys.stdin.readline().split()) # 수첩2에 적혀있는 정수들 m개

    for i in m_data:
        if i in n_data:
            print(1)
        else:
            print(0)
