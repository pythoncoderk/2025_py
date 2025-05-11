l = [2, 5, 1, 4, 6, 3]

for i in range(len(l)):
    min_l = i
    for j in range(i, -1, -1):
        if l[min_l] < l[j]:
            l[min_l], l[j] = l[j], l[min_l]
            min_l = j

print(l)
