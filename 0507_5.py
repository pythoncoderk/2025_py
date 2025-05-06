s = list(input())

print(s)

for i in range(1 << len(s)):
    l = []
    for j in range(len(s)):
        if i & (1 << i):
            l.append("o")
        else:
            l.append("x")
    print(l)