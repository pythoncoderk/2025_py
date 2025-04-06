n, m = map(int, input().split())
l = list(map(int, input().split()))

ans = -1
for i in range(len(l)):
    if l[i] >= m:
        ans = i
        break

print(ans)