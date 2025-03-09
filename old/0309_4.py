n = int(input())

l = []
for i in range(n):
    l2 = []
    for j in range(n):
        l2.append("?")
    l.append(l2)

print(l)

for i in range(n):
    for j in range(n):
        x = n + 1 - i + 1
        if i <= x:
            if i % 2 == 0 and i != 0:
                l[i][j] = "."
            else:
                l[i][j] = "#"

print(l)
