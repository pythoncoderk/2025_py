n, c1, c2 = map(str, input().split())
s = input()

ans = ""
for i in s:
    if i != c1:
        ans += c2
    else:
        ans += i

print(ans)