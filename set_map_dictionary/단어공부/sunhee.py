import sys

word=sys.stdin.readline().strip().upper()
alpha=list(set(word))

count=[]

for i in alpha:
    count.append(word.count(i))

maxnum=max(count)

if count.count(max(count))>1:
    print("?")
else:
    print(alpha[count.index(maxnum)].upper())


