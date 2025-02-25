n = int(input())
l = []

for _ in range(n):
    x = input()
    if x in l:
        x_i = 0
        for i in range(len(l)):
            if l[i] == x:
                xi = i
        l.pop(xi)
        l.insert(0, x)
    else:
        l.insert(0, x)

for _ in l:
    print(_)
