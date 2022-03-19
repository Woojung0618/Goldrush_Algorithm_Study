#신입사원 문제는 성적이나 면접 중 둘 중 하나가 남들보다 뛰어나면 입사
#성적 순위를 높은 순으로 정렬
#성적 1등은 성적이 남들보다 우수하니 무조건 입사 +1
#성적 2등은 성적 1등보다 성적 순위는 낮지만 면접 순위가 높다면 남들보다 우수한 것이 있는 것이니 count+1

import sys

for _ in range(int(sys.stdin.readline())):
    t_list=[]
    for _ in range(int(sys.stdin.readline())):
        a,b=map(int,sys.stdin.readline().split())
        t_list.append((a,b))
    t_list.sort()

    count=1
    rank=t_list[0][1]

    for a,b in t_list[1:]:
        if b<rank:
            rank=b
            count+=1

    print(count)

