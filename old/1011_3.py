n = int(input())

x = 1
l = []
for i in range(n):
    y = str(x)
    for j in y:
        l.append(int(j))
    x = sum(l)

print(sum(l))