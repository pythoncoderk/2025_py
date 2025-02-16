n = int(input())

l = []

for i in range(n):
    x = input()
    if x in l:
        y = l.index(x)
        l.pop(y)
        l.insert(0, x)
    else:
        l.insert(0, x)
for i in l:
    print(i)