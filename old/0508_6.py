n = input()
for i in range(1 << len(n) - 1):
    l = []
    for j in range(len(n) - 1):
        if i & (1 << j):
            l.append("o")
        else:
            l.append("x")
    print(l)