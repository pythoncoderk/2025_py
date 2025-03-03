l = list(map(str, input().split()))

d = {}
for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

for i, j in d.items():
    print(i, j)