n, p, q = map(int, input().split())
l = list(map(int, input().split()))

ans_l = []

for i in range(n):
    ans_l.append(q + l[i])

print(min(p, min(ans_l)))