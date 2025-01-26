h, w, n = map(int, input().split())

l = [list(input()) for i in range(h)]

for i in range(n):
    x, y = map(int, input().split())
    l[x][y] = "#"

for i in l:
    print("".join(i))