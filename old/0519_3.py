n = input()
ans = 0
for i in range(len(n)):
    kake = 2 ** (len(n) - 1 - i)
    ans += int(n[i]) * kake

print(ans)