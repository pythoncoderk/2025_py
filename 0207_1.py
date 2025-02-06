import copy

m, n = map(int, input().split())

l = [i for i in range(1, m + 1)]
l3 = l[:]
for i in range(n):
    l2 = []
    for j in range(m // 2):
        l2.append(l3[j + m // 2])
        l2.append(l3[j])
    l3 = copy.deepcopy(l2)

print(*l3)