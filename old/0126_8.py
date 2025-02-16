n = int(input())

l = [int(input()) for i in range(n)]

print(l)

x, y = 1, 1
a, b = 1, 1
for i in range(n-1, -1, -1):
    y = l[i]
