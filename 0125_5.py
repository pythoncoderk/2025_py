h, w = map(int, input().split())

l = [list(input()) for i in range(h)]

# print(l)

for i in range(h):
    for j in range(w):
        if i == 0:
            if l[i + 1][j] == "#":
                print(i, j)
        elif i == h - 1:
            if l[i - 1][j] == "#":
                print(i, j)
        else:
            if l[i + 1][j] == "#" and l[i - 1][j] == "#":
                print(i, j)
