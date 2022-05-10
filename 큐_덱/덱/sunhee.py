from collections import deque
import sys

input=sys.stdin.readline
stack=[]
stack=deque(stack)
for _ in range(int(input())):
    a=input().split()
    if a[0]=='push_front':
        stack.appendleft(a[1])  #가장 앞에 넣기
    elif a[0]=='push_back':
        stack.append(a[1])      #가장 뒤에 넣기
    elif a[0]=='front':
        if len(stack)!=0:   
            print(stack[0])     #가장 앞에 있는 정수 출력
        else:
            print(-1)
    elif a[0]=='back':
        if len(stack)!=0:
            print(stack[-1])    #가장 뒤에 있는 정수 출력
        else:
            print(-1)
    elif a[0]=='pop_front':     #덱의 가장 앞에 있는 수를 빼고 그 수 출력
        if len(stack)!=0:
            print(stack.popleft())
        else:
            print(-1)
    elif a[0]=='pop_back':      #덱의 가장 뒤에 있는 수를 빼고 그 수 출력
        if len(stack)!=0:
            print(stack.pop())
        else:
            print(-1)
    elif a[0]=='size':          #덱 사이즈
        print(len(stack))  
    elif a[0]=='empty':         #덱 비어있는지 확인
        if len(stack):
            print(0)
        else:
            print(1)
