import sys

for i in range(int(sys.stdin.readline())):
    testcase=list(sys.stdin.readline().split())
    testcase.reverse()
    print("Case #%d:" %(i+1),end=" " )
    for j in testcase:
        print(j,end=" ")
    print()