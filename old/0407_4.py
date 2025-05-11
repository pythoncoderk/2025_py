l = ["A", "B", "C", "D", "E"]

n = len(l)
for i in range(2 ** n):
    l2 = []
    for j in range(n):
        if i >> j & 1:
            l2.append(l[j])
    print(l2)