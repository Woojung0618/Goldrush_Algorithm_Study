# 서류 점수로 오름차순 정렬(순위를 나타내기 때문에!!!)
# count 변수는 선발될 사람의 수로 서류점수 1등은 바로 합격이기 때문에 1로 세팅
# 더 좋은 서류점수를 가진 사람들보다 면접 성적이 좋아야 뽑힘 -> 이때, 각각을 비교하면 시간초과!

# 서류점수 1등 지원자의 면접점수를 변수에 저장해두고 나머지 지원자들의 면접점수와 비교
# 서류점수 1등 지원자의 면접점수보다 높으면 그 점수를 min에 저장하고 count 변수 증가시킴!
import sys

t = int(input())

for _ in range(t):
    n = int(input())
    data = sorted([list(map(int, sys.stdin.readline().strip().split())) for x in range(n)], key = lambda x: x[0])
    
    '''
    # 시간초과 코드 ?? -> 같은 for문을 썼는데...??
    for _ in range(n):
        data.append(list(map(int, sys.stdin.readline().split())))
        data.sort()
    '''
    count = 1
    min = data[0][1]

    for i in range(1, n):
        if (data[i][1] < min):
            min = data[i][1]
            count += 1
    print(count)