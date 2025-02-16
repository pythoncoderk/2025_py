y, x, d = map(str, input().split())

y = int(y)
x = int(x)

l_r = input()

if d == "N":
    if l_r == "R":
        x += 1
    else:
        x -= 1
elif d == "S":
    if l_r == "R":
        x -= 1
    else:
        x += 1
elif d == "W":
    if l_r == "R":
        y -= 1
    else:
        y += 1
else:
    if l_r == "R":
        y += 1
    else:
        y -= 1

print(y, x)