n = int(input())

l = [list(map(int, input().split())) for i in range(n)]

# print(l)

l2 = []
for i in range((n + 1) // 2):
    l3 = []
    for j in range((n + 1) // 2):
        if i > j:
            l3.append(j + 1)
        else:
            l3.append(i + 1)
    l2.append(l3)

# print(l2)

l4 = []
for i in range(len(l2)):
    l5 = sorted(l2[i], reverse=True)
    l4.append(l2[i] + l5[1:])

l6 = sorted(l4, reverse=True)

l9 = l4 + l6[1:]

ans = 0
for i in range(n):
    for j in range(n):
        ans += l[i][j] - l9[i][j]
print(ans)