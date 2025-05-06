n = input()
x = len(n) - 1
a = list(n)

for i in range(1 << x):
    b = []
    for j in range(x):
        if i & (1 << j):
            b.append("+")
        else:
            b.append("")
    print(b)
    l = []
    ans = ""
    for xxx in range(len(n)-1):
        ans += a[xxx]
        ans += b[xxx]