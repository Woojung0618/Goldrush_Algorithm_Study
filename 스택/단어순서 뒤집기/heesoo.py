# 입력을 받자마자 각 case들을 출력
import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    # whitespace을 사용해서 데이터를 가공할 시에 문제가 될 수도 있으므로 strip()을 사용해서 제거해줌!
    word = list(sys.stdin.readline().rstrip().split())

    # join함수는 문자열을 합쳐준다. 
    # string 사이에 특정 문자열을 삽입하여 나눠져 있던 문자열을 새로운 문자열로 합쳐줌 

    # 슬라이싱 
    # -> [start:end:step]으로 1,2번째에 아무런 값도 주지 않으면 모든 값을 의미
    # -> 이때, 3번째 증감에서 -1을 처리하면 맨 뒤에서부터 역순으로 하나씩 슬라이싱한 것!!
    print("Case #%d: %s" %(i, ' '.join(word[::-1])))
