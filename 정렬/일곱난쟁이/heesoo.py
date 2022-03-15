# 9명 중 두명을 빼서 그 합이 100이 나오면 된다!

lengths = [int(input()) for i in range(9)]
s_sum = sum(lengths)

for i in range(8):
    for j in range(i+1, 9):
        if s_sum - (lengths[i] + lengths[j]) == 100:
            delete_one = lengths[i]
            delete_two = lengths[j]
            
lengths.remove(delete_one)
lengths.remove(delete_two)

lengths.sort()
for k in lengths:
    print(k)