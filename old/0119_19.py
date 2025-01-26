h, w, n = map(int, input().split())

l1 = [list(input()) for i in range(h)]
l2 = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    l1[l2[i][0]][l2[i][1]] = "#"

for i in range(h):
    print("".join(l1[i]))