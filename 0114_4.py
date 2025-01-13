def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)




n = int(input())
l = [int(input()) for i in range(n)]
for i in range(n-1):
    x = l.pop(0)
    y = l.pop(0)
    l.insert(0, gcd(x, y))

print(l[0])

