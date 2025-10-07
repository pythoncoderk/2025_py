n = int(input())

ans = 0
for i in range(n):
    x = i + 1
    y = (-1) ** x * (x ** 3)
    ans += y

print(ans)