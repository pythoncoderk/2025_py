n = int(input("n = "))
for bit in range(1 << n):
    b = []
    for i in range(n):
        if bit & (1 << i):
            b.append(1)
        else:
            b.append(0)
    print(b)