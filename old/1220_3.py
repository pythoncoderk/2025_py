h, w, n = map(int, input().split())
l = []
for i in range(h):
    l2 = list(map(int, input().split()))
    l.append(l2)

l5 = []
for i in range(n):
    l5.append(int(input()))

ans = 0
for i in range(h):
    x = set(l[i]) & set(l5)
    ans = max(len(x), ans)
print(ans)