y, x, n = map(int, input().split())

l = [input() for i in range(n)]

# print(l)

for i in l:
    if i == "N":
        y -= 1
        print(y, x)
    elif i == "S":
        y += 1
        print(y, x)
    elif i == "W":
        x -= 1
        print(y, x)
    else:
        x += 1
        print(y, x)
