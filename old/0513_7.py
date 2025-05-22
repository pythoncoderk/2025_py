n = int(input())
ans = ""

while n >= 1:
    if n % 2 == 0:
        ans += "0"
    else:
        ans += "1"
    n //= 2

ans_f = ans[::-1]
print(ans_f.zfill(10))