n, m = map(int, input().split())
s = input()
t = input()
ans = 10**9
for st in range(n - m + 1):
    res = 0
    for i in range(m):
        res += (int(s[st + i]) - int(t[i])) % 10
    ans = min(ans, res)
print(ans)
