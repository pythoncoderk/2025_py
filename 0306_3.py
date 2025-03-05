n = int(input())
ans = 0
bit = 1

while bit <= n:
    if bit & n != 0:
        ans += 1
    bit *= 2

print(ans)