n, m = map(int, input().split())
g = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))

for i in range(n):
    print(f"{i}: {g[i]}")