n = int(input())
l = list(map(int, input().split()))

ans = 0
for i in range(n):
    if (i +1) % 2 != 0:
        ans += l[i]

print(ans)
