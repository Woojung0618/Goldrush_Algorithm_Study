import sys

for _ in range(int(sys.stdin.readline())):
    p=sys.stdin.readline().strip()
    n=int(sys.stdin.readline())
    nlist=sys.stdin.readline()[1:-2].split(',')

    if len(nlist)==1 and nlist[0]=='':
        nlist=[]
    else:
        nlist=list(map(int,nlist))

    for i in p:
        if i=='R':
            nlist.reverse()
        else:
            if(len(nlist)!=0):
                nlist.pop(0)
            else:
                print('error')
                break
    else:
        print(nlist)