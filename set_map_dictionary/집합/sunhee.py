import sys

slist=set()
for i in range(int(sys.stdin.readline())):
    m=sys.stdin.readline().split()

    if len(m)==1:
        if m[0]=='all':
            slist=set([i for i in range(1,21)])
        elif m[0]=='empty':
            slist=set()
    else:
        a,b=m[0],m[1]
        b=int(b)
        if a=='add':
            slist.add(b)
        elif a=='remove':
            slist.discard(b)
        elif a=='check':
            if b in slist: print(1)
            else: print(0)
        elif a=='toggle':
            if b in slist:
                slist.discard(b)
            else:
                slist.add(b)
