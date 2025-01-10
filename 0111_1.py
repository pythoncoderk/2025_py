x, y, n = map(int, input().split())
neet = n
r = n // 3
n = neet
# print(r)

total = [x * n]
t = 0
if r > 0:

    for i in range(1, r + 1):
        n = neet
        n -= 3 * i
        t += y * i
        while n > 0:
            n -= 1
            t += x
        total.append(t)
        t = 0
print(min(total))
