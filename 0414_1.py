s = input()
l2 = []
for i in range(1 << len(s)):
    l = []
    for j in range(len(s)):
        if i & 1 << j:
            l.append(1)
        else:
            l.append(0)

    print(l)