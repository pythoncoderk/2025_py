l = list(map(str, input().split()))
l2 = []
for _ in range(len(l)):
    if l[_] not in l2:
        print(l[_])
        l2.append(l[_])
    else:
        print(l2.count(l[_]))