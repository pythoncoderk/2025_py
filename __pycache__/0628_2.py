n = int(input())
ans = 0
for i in range(n):
    x, y = map(int, input().split())
    if x < y:
        ans += 1
print(ans)