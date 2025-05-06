n = int(input())

for i in range(1 << n):
    l = []
    for j in range(n):
        if i & (1 << j):
            l.append("o")
        else:
            l.append("x")
    print(l)