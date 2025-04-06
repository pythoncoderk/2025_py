ab, ac, bc = map(str, input().split())

a = 0
b = 0
c = 0

if ab == "<":
    a += 0
    b += 1
else:
    a += 1
    b += 0

if ac == "<":
    a += 0
    c += 1
else:
    a += 1
    c += 0
if bc == "<":
    b += 0
    c += 1
else:
    b += 1
    c += 0

l = [a, b, c]

if l[0] == 1:
    print("A")
elif l[1] == 1:
    print("B")
else:
    print("C")