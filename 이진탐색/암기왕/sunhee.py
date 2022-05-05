import sys

def find(num, nlist):
    lt=0
    rt=len(nlist)-1
    while lt<=rt:
        mid=(lt+rt)//2
        if nlist[mid]==num:
            print(1)
            return
        elif nlist[mid]<num:
            lt=mid+1
        else:
            rt=mid-1
    print(0)
    return

for _ in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    nlist=list(map(int,input().split()))
    nlist.sort()
    m=int(sys.stdin.readline())
    mlist=list(map(int,input().split()))

    for num in mlist:
        find(num, nlist)
        
        
