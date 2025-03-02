n = int(input())

target = [["?"] * n for _ in range(n)]


for i in range(n):
    j = n - i - 1
    if i <= j:
        for x in range(i, j + 1):
            for y in range(i, j + 1):
                if i % 2 == 0:
                    target[x][y] = "#"
                else:
                    target[x][y] = "."

for row in target:
    print("".join(row))