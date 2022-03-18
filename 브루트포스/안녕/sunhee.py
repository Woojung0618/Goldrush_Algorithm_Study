import sys

n=int(sys.stdin.readline())
health=list(map(int,sys.stdin.readline().split()))  #손님별 체력
happy=list(map(int,sys.stdin.readline().split()))   #손님별 행복
hh_list=[]
for i in range(n):
    a=health[i]
    b=happy[i]
    hh_list.append((a,b))   #손님별로 체력과 행복을 함께 리스트에 넣어줌
hh_list.sort(key=lambda x:(x[1],x[0]),reverse=True) #최대 행복을 구하는 것이므로 행복이 높은 순으로 정렬

health_max=100  #나의 체력=100
happy_size=0    #앞으로 채워질 행복
for a,b in hh_list:
    if health_max-a<=0: #내 체력에서 손님의 체력을 뺐을때 0보다 작으면 다음 걸로
        continue
    else:
        health_max-=a
        happy_size+=b
    if health_max<=0:
        break

print(happy_size)

