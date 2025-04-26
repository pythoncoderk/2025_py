l = list(map(str, input().split()))
l2 = []

for i in range(len(l)):
    if l[i] in l2:
        print(1)
    else:
        l2.append(l[i])
        print(l[i])