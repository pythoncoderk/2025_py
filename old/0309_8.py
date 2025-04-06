n, m = map(int, input().split())
l = list(map(int, input().split()))

l2 = [i for i in range(1, n + 1)]

l3 = []
for i in l2:
    if i not in l:
        l3.append(i)
print(len(l3))
print(*l3)