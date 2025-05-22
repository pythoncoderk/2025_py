n, k = map(int, input().split())
count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        z = k - i - j
        if z >= 1 and z <= n:
            count += 1
print(count)
