m, d = map(int, input().split())
y, mm, dd = map(int, input().split())

if dd + 1 > d:
    dd = 1
    mm += 1
else:
    dd += 1

if mm > m:
    mm = 1
    y += 1


print(y, mm, dd)