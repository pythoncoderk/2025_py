s = input()
o = []
h = []
x = []
for i in range(9):
    if s[i] == "o":
        o.append(str(i))
    elif s[i] == "x":
        h.append(str(i))
    else:
        x.append(str(i))

print(o)
print(h)
print(x)