#이중for문, while문 안에 for문 써봤지만 둘 다 시간초과가 났고 생각해보니 둘 다 정렬 알고리즘을 사용하지 않아서
#구글링을 하여 어떤 알고리즘을 사용하는지 확인 -> 투포인터 사용
#start=0, end=(리스트 사이즈-1)해서 start+end<m이면 start+1
#start+end<m이면 end-1

import sys

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
n_list=list(map(int,sys.stdin.readline().split()))
n_list.sort()

c_count=0

start=0
end=len(n_list)-1

while start<end:
    if n_list[start]+n_list[end]<m:
        start+=1
    elif n_list[start]+n_list[end]>m:
        end-=1
    else:
        c_count+=1
        end-=1

print(c_count)


#시간초과 코드 + 정렬 알고리즘 사용X
#n_idx=0
# while n_list:
#     if n_idx==len(n_list)-1:
#         break
#     for i in range(n_idx+1,len(n_list)):
#         if n_list[n_idx]+n_list[i]==m:
#             a=n_list.pop(n_idx)
#             b=n_list.pop(i-1)
#             c_count+=1
#             break
#     else:
#        n_idx+=1