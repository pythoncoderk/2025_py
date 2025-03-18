n = int(input())
l = list(map(int, input().split()))

ans = 0
for i in range(1, n):
    x = len(set(l[:i]))
    y = len(set(l[i:]))
    if ans < x + y:
        ans = x + y

print(ans)