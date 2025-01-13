n, k = map(int, input().split())

l = [list(map(int, input().split())) for i in range(n)]

l2 = []
for i in range(k):
    l3 = []
    for j in range(n):
        l3.append(l[j][i])
    l2.append(l3)

ans = []
for i in range(k):
    min_l = l2[i][0]
    min_j = 0
    for j in range(n):
        if l2[i][j] < min_l:
            min_l = l2[i][j]
            min_j = j
    ans.append(min_j)

print(len(set(ans)))