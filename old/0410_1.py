n, m = map(int, input().split())

ans = n
total = 1
for i in range(m - 1):
    total += ans
    ans *= n

total += ans
print(total if total <= 1000000000 else "inf")