n, m = map(int, input().split())
l = list(map(int, input().split()))

ans = 0
for i in range(n):
    ans += l[i] // 100

if (m - ans) * 100 <= 0:
    print(0)
else:
    print((m - ans) * 100)