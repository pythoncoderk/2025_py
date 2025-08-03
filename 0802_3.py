from collections import deque

n, m = map(int, input().split())
da = deque(list(map(int, input().split())))
l = list(map(int, input().split()))

for i in range(len(l)):
    if da.count(l[i]) >= 1:
        da.remove(l[i])
print(*da)
