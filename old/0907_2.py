n, m = map(int, input().split())
l = []
flag = True
for i in range(n):
    l2 = []
    x = list(input())
    if x.count('#') >= 1:
        flag = False
    l.append(x)

l_flag = True

for i in range(n):

    for j in range(m):
        chk = 0
        if l[i][j] == "#":
            l_flag = False
            if i - 1 >= 0:
                if l[i-1][j] == "#":
                    chk += 1
        if l[i][j] == "#":
            l_flag = False
            if i + 1 <= n-1:
                if l[i+1][j] == "#":
                    chk += 1
        if l[i][j] == "#":
            l_flag = False
            if j - 1 >= 0:
                if l[i][j-1] == "#":
                    chk += 1
        if l[i][j] == "#":
            l_flag = False
            if j + 1 <= m-1:
                if l[i][j+1] == "#":
                    chk += 1
        if chk == 2 or chk == 4:
            l_flag = True

print("Yes" if l_flag else "No")
