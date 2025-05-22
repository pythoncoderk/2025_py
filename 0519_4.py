n = int(input("n = "))
for bit in range(1 << n):
    b = []
    for i in range(n):
        if (bit & (1 << i)):
            b.append("o")
        else:
            b.append("x")
    print(b)