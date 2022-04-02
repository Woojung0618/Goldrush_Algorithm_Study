
string = list(input())
stack = []

for s in range(len(string)): 
    if string[s] == '(' or string[s] == '[':
        stack.append(string[s])

    elif string[s] == ')':
        tmp = 0
        while stack:
            top = stack.pop()
            if top == '[':
                print(0)
                exit(0)
            elif top == '(':
                if tmp == 0:
                    stack.append(2)
                else:
                    stack.append(2 * tmp)
                break
            else:
                tmp += top

    elif string[s] == ']':
        tmp = 0
        while stack:
            top = stack.pop()
            if top == '(':
                print(0)
                exit(0)
            elif top == '[':
                if tmp == 0:
                    stack.append(3)
                else:
                    stack.append(3 * tmp)
                break
            else:
                tmp += top

# print(stack)
answer = 0
for i in stack:
    if i == '(' or i == '[' or i == ')' or i == ']':
        print(0)
        exit(0)
    else:
        answer += i
print(answer)