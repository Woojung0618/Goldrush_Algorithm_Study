import sys
word = sys.stdin.readline().rstrip()
word = word.upper()
dict = {}
for w in word:
    if w in dict:
        dict[w] += 1
    else:
        dict[w] = 1
max_value = max(dict.values())
count = 0
answer = ''
print(dict.values())

for d in dict:
    if dict[d] == max_value:
        answer = d
        count += 1
    
if count == 1:
    print(answer)
else:
    print('?')
