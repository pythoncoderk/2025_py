n = int(input())

ans = ""
for i in range(n):
    ans += "-"

if n % 2 == 0:
    for i in range(n):
        if i + 1 == n // 2:
            