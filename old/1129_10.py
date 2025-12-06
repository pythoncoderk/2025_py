h, w = map(int, input().split())

l = []
for i in range(h):
    x = list(input())
    l.append(x)

for i in range(h):
    count = 0
    for j in range(w):
        if l[i][j] == "#":
            print("#", end="")
        else:
            if i == 0:
                pass
            else:
                if l[i-1][j] == "#":
                    count += 1
            if i == w-1:
                pass
            else:
                if l[i-1][j] == "#":
    print()


