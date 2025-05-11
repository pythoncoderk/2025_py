n = int(input("n = "))
count = 1
for bit in range(1 << n):
    b = []
    for i in range(n):
        if (bit & (1 << i)):
            b.append(1)
        else:
            b.append(0)
    print(str(count) + " " + str(b))
    count += 1