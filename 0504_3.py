l = [2, 5, 1, 4, 6, 3]

for i in range(len(l)):
    min_l = 100
    index_l = 0
    for j in range(i, len(l)):
        if min_l > l[j]:
            min_l = l[j]
            index_l = j
    l[i], l[index_l] = l[index_l], l[i]

print(l)
