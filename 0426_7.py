l = list(map(str, input().split()))
l2 = []

for i in l:
    if i not in l2:
        l2.append(i)

for i in l2:
    print(i)

for i in l2:
    print(l.count(i))