h, w = map(int, input().split())

l = [list(input()) for i in range(h)]

for i in range(h):
    for j in range(w):
        if l[i][j] == "#":
            print(i, j)

