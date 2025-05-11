n = int(input())
ans = ""

while n >= 1:
    if n >= 0:
        x = n % 2
        if x == 0:
            ans += "0"
        else:
            ans += "1"
    n //= 2

ans = ans[::-1]
print(ans.zfill(10))