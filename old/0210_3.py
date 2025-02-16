n, k = map(int, input().split())
l = list(map(int, input().split()))

l2 = []
for i in range(n):
    if l[i] % k == 0:
        l2.append(l[i] // k)

l2.sort()
print(*l2)