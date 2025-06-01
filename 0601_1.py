n, m = map(int, input().split())
imos = [0] * (n + 1)
for _ in range(m):
    l, r = map(int, input().split())
    l -= 1
    imos[l] += 1
    imos[r] -= 1
for i in range(1, n + 1):
    imos[i] += imos[i - 1]
ans = 1e9
for i in range(n):
    ans = min(ans, imos[i])
print(ans)
