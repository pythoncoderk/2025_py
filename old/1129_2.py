n, m = map(int, input().split())
l = []
for i in range(n):
    x, y = map(int, input().split())
    l.append([x-1, y])

l2 = []
for i in range(m):
    l2.append([0, 0])

for i in range(n):
    l2[l[i][0]][0] += 1
    l2[l[i][0]][1] += l[i][1]

for i in range(m):
    print(l2[i][1] / l2[i][0])