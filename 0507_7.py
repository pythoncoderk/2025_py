n = int(input())

for i in range(1 << n):
    b = []
    for j in range(n):
        if i & (1 << j):
            b.append("o")
        else:
            b.append("x")
    print(b)