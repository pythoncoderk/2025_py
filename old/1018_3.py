l = input().split()
l2 = []
l3 = []

for i in l:
    if i not in l2:
        l2.append(i)
        print(i)
        l3.append(1)
    else:
        l3[l2.index(i)] += 1

for i in l3:
    print(i)
