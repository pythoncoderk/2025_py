import itertools

n = int(input())
l = []
for i in range(n):
    l.append(input())

ans_l = []
for i in range(n):
    ans = l[i]
    for j in range(n):
        if i != j:
            ans += l[j]
            ans_l.append(ans)
            ans = l[i]
ans_set = set(ans_l)
print(len(ans_set))