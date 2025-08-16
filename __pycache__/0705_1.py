n, m = map(int, input().split())
l = list(map(int, input().split()))

print("Yes" if sum(l) <= m else "No")