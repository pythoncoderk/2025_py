n, m = map(int, input().split())
l = []
for i in range(m):
    x, y = map(int, input().split())
    l2 = [x-1, y]

    l.append(l2)

l3 = [0] * n
for i in range(m):
    l3[l[i][0]] = l[i][1]
    if l3.count(0) == 0:
        print(sum(l3))
        exit()

print(0)
