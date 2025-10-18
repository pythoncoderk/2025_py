l = []
n = int(input())
for i in range(n):
    s = input()
    if s in l:
        y = l.index(s)
        l.remove(s)
        l.insert(0, s)
    else:
        l.insert(0, s)

for i in l:
    print(i)