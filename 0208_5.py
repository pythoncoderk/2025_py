n, m = map(int, input().split())

l = list(map(int, input().split()))

l2 = []
for i in range(1, n + 1):
    if i not in l:
        l2.append(i)

print(len(l2))

if len(l2) != 0:
    print(*l2)