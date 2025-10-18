l = input().split()
l2 = []

for i in l:
    if i not in l2:
        print(i)
        l2.append(i)
    else:
        print(l2.index(i))

