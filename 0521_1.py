n, m = map(int, input().split())
count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        k = m - i - j
        if 1 <= k <= n:
            count += 1
print(count)
