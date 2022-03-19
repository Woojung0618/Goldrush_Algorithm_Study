height = [int(input()) for _ in range(9)]

for i in range(9):
    for j in range(i+1, 9):
        if sum(height) - (height[i] + height[j]) == 100:
            del height[i]
            del height[j]
            break

for n in range(10):
    print(height[n])