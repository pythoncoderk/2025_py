n = int(input())
flag = True

if n % 2 == 0:
    x = n // 2
    y = x + 1
else:
    x = n // 2 + 1
    flag = False

ans = ""
if flag:
    for i in range(n):
        if i + 1 != x and i + 1 != y:
            ans += "-"
        else:
            ans += "="
else:
    for i in range(n):
        if i + 1 != x:
            ans += "-"
        else:
            ans += "="

print(ans)


