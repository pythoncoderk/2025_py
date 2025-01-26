l = list(map(str, input().split()))

l2 = []

for i in l:
    if i in l2:
        print(1)
    else:
        l2.append(i)
        print(i)