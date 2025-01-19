n, x = map(int, input().split())
ans = ""
for i in range(65, 91):
    for j in range(n):
        ans += chr(i)

print(ans[x-1])