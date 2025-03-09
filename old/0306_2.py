n = int(input())
ans = 0
bitmastk = 1

while bitmastk <= n:
    if bitmastk & n != 0:
        ans += 1
    bitmastk *= 2

print(ans)