n, m, x, t, d = map(int, input().split())

# print(n, m, x, t, d)

tall = x * d
min = t - tall

# print(tall)
# print(min)

if x <= m <= n: print(t)
else: print(min + d * m)
