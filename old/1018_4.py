s, a, b, x = map(int, input().split())

n = 0
flag = True
m = 0
ans = 0
while True:
    if flag:
        if n + a >= x:
            if n <= x:
                ans += (x - m) * s
                break
            else:
                break
        else:
            n += a
            m = n
            ans += a * s
            flag = False
    else:
        n += b
        m = n
        flag = True

print(ans)