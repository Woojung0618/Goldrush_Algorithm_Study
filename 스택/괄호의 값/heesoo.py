# 4개의 기호 ( ) * 2 [ ] * 3 -> 올바른 괄호열
# X가 올바른 괄호열 -> (X) [X]
# X와 Y 모두 올바른 괄호열 -> 이들을 결합한 XY도 올바른 괄호열, (X) + (Y)

# 왜 stack_list가 아닌 data에서 비교할까??
import sys

stack_list = []
result = 0
temp = 1
data = list(input())


for i in range(len(data)):
    if (data[i] == "("):
        temp *= 2
        stack_list.append(data[i])
    elif (data[i] == "["):
        temp *= 3
        stack_list.append(data[i])
    elif (data[i] == ")"):
        # 인덱스 -1은 마지막 값을 나타낸다.
        if not stack_list or stack_list[-1] == "[":
            result = 0
            break
        if data[i-1] == "(":
            result += temp
        stack_list.pop()
        temp //= 2
    else:
        if not stack_list or stack_list[-1] == "(":
            result = 0
            break
        if data[i-1] == "[":
            result += temp
        stack_list.pop()
        temp //= 3

if stack_list:
    print(0)
else:
    print(result)


