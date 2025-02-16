n, k, x = map(int, input().split())
l = list(map(int, input().split()))

l.insert(k, x)
print(*l)