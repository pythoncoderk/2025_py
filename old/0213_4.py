n, k = map(int, input().split())
l = list(map(int, input().split()))

x = l[k * -1:]
y = l[:k * -1]

ans = x + y

print(*ans)