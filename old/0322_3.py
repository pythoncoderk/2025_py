n = int(input())

ans = ""
for i in range(n):
    if n % 2 == 0:
        if i + 1 == n // 2 or i + 1 == (n // 2) + 1:
            ans += "="
        else:
            ans += "-"
    else:
        if i == n // 2:
            ans += "="
        else:
            ans += "-"

print(ans)