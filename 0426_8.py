l = list(map(str, input().split()))
l2 = []
l3 = []

for i in range(len(l)):
    if l[i] not in l2:
        l2.append(l[i])

for i in l2:
    print(i, end=" ")
    print(l.count(i))