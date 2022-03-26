from collections import deque
import sys

stack=[]
bracket=list(sys.stdin.readline())
bracket=deque(bracket)

for i in range(len(bracket)-1):
    a=bracket.popleft()
    if a=='[' or a=='(':
        stack.append(a)
    elif a==')':
        num=0
        if len(stack)==0:
            print(0)
            exit()
        while stack:
            top=stack.pop()
            if top=='(':
                if num==0:
                    stack.append(2)
                else:
                    stack.append(2*num)
                break
            elif top=='[':
                print(0)
                exit()
            else:
                num+=top
    elif a==']':
        num=0
        if len(stack)==0:
            print(0)
            exit()
        while stack:
            top=stack.pop()
            if top=='[':
                if num==0:
                    stack.append(3)
                else:
                    stack.append(3*num)
                break
            elif top=='(':
                print(0)
                exit()
            else:
                num+=top       
else:
    if '[' in stack:
        print(0)
    elif '(' in stack:
        print(0)
    elif ')' in stack:
        print(0)
    elif ']' in stack:
        print(0)
    else:
        print(sum(stack))
