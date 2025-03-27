l = list(map(int, input().split()))

l2 = []
for i in l:
    l2.append(l.count(i))

l3 = set(l2)
print(l3)

