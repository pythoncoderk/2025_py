l = [2, 5, 1, 4, 6, 3]

for i in range(len(l)):
    min_l = l[i]
    index_min = i
    for j in range(i, len(l)):
        if min_l > l[j]:
            min_l = l[j]
            index_min = j
    l[i], l[index_min] = l[index_min], l[i]

print(l)
