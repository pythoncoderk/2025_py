import itertools

n = int(input())
l = list(map(int, input().split()))
l2 = []
for i in itertools.combinations(l, 3):
    l2.append(i)

ans = 0
for i in l2:
    x = set(i)
    if len(x) == 2:
        ans += 1
print(ans)
