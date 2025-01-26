h, w = map(int, input().split())

l = [list(input()) for i in range(h)]

count = 0
for i in range(h):
    for j in range(w):
        if j == 0:
            if l[i][j + 1] == "#":
                print(i, j)
        elif j == w - 1:
            if l[i][j - 1] == "#":
                print(i, j)
        else:
            if l[i][j - 1] == "#" and l[i][j + 1] == "#":
                print(i, j)

