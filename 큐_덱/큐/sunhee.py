import queue
import sys

input=sys.stdin.readline
stack=[]
for _ in range(int(input())):
    a=input().split()
    if a[0]=='push':
        stack.append(a[1])  #가장 앞에 넣기
    elif a[0]=='pop':
        if len(stack)!=0:
            print(stack.pop(0))     
        else:
            print(-1)
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
    elif a[0]=='size':          #덱 사이즈
        print(len(stack))  
    elif a[0]=='empty':         #덱 비어있는지 확인
        if len(stack):
            print(0)
        else:
            print(1)
