#12605번 단어순서 뒤집기

import random

num = int(input())
n=1

for i in range(num):
    word = input().split(' ')
    word.reverse()
    print("Case #%d:"%n , *word, sep = ' ')
    n += 1
