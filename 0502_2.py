n = int(input())
ans = 0
while n >= 500:
    n -= 500
    ans += 1
while n >= 100:
    n -= 100
    ans += 1
while n >= 50:
    n -= 50
    ans += 1
while n >= 10:
    n -= 10
    ans += 1
while n >= 5:
    n -= 5
    ans += 1
while n >= 1:
    n -= 1
    ans += 1

print(ans)