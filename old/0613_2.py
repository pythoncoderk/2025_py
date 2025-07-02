l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(sum([2, 3, 4, 5, 6, 7, 8]))
l2 = [0]
total = 0
for i in range(len(l)):
    l2.append(total + l[i])
    total += l[i]

# print(l2)
print(l2[7+1] - l2[2-1])