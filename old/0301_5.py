n = int(input())

if n % 2 == 0:
    x = n // 2
else:
    x = n // 2 + 1

l = [list("*" * n) for i in range(x)]

for q in range(n):
    for i in range(q, x):
        if q == 0:
            for j in range(n):
                if q % 2 == 0:
                    l[i][j] = "#"
                else:
                    l[i][j] = "."
        else:
            for j in range(q, n):
                if q % 2 == 0:
                    l[i][j] = "#"
                else:
                    l[i][j] = "."
print(l)


