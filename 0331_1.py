n = int(input())
l = []
for i in range(n):
    x = input()
    if x not in l:
        l.insert(0, x)
    else:
        for j in range(len(l)):
            if l[j] == x:
                del l[j]
                l.insert(0, x)
                break

for i in l:
    print(i)
