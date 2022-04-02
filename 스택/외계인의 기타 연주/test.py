n, p = map(int, input().split())
# 프렛 번호 p개
# 현재 누른 프렛 번호보다 더 큰 숫자의 프렛 번호를 누를 때는 손가락을 떼지 않고 이동할 수 있음
# 줄 번호 마다 stack 생성 stack[줄] = [프렛] list
stacks = [[] for _ in range(6)]
for _ in range(n):
    i, j = map(int, input().split())
    stacks[i].append(j)
# print(stacks)

def calc_count(stack):
    count = 0
    line_stack = []
    print(stack)
    for s in stack:
        # print('this is ', s)
        
        if line_stack:
            if line_stack[-1] < s:  # top보다 누를 프렛이 더 크면, 한번 증가
                count += 1
                line_stack.append(s)
                # print('#22 ', count)
            elif line_stack[-1] > s:  # top보다 누를 프렛이 더 작으면
                while line_stack:  # 프렛보다 작은 애가 나올 때까지 pop, count + 1
                    if line_stack[-1] > s:
                        line_stack.pop()
                        count += 1
                    else:
                        break
                    # print('#30 ', count)
                line_stack.append(s)
            elif line_stack[-1] == s:  # top과 누를 프렛이 같다면, 처리 X
                # print('#33 ', count)
                pass
        else:  # 스택 비어있으면 append, count +1. 아무것도 없으면 눌러야하니까
            line_stack.append(s)
            count += 1
            # print('#38 ', count)    
    print(count)
    return count

answer = 0
for stack in stacks:
    if stack:
        answer += calc_count(stack)

print(answer)