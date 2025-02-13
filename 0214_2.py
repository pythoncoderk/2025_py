a, b, c = map(str, input().split())

# print(a, b, c)

l = [0, 0, 0]
if a == "<":
    l[1] += 1
else:
    l[0] += 1

if b == "<":
    l[2] += 1
else:
    l[0] += 1

if c == "<":
    l[2] += 1
else:
    l[1] += 1

if l[0] == 1:
    print("A")
elif l[1] == 1:
    print("B")
else:
    print("C")