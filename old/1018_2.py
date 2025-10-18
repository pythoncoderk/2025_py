l = input().split()
l2 = []
l3 = {}
l4 = []

for i in l:
    if i not in l2:
        l2.append(i)
        l3[i] = 1
    else:
        l3[i] += 1

for i in l2:
    l4.append(l3[i])

for i in l2:
    print(i)
for i in l4:
    print(i)

