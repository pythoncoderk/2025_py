n, m, k = map(int, input().split())

l = []
for i in range(n):
    l2 = [0] * m
    l.append(l2)

ans = []

for i in range(k):
    x, y = map(int, input().split())
    l[x - 1][y - 1] = 1
    for j in range(n):
        if sum(l[j]) == m:
            ans.append(j+1)
            l[j][0] = 0
print(*ans)