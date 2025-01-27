n = int(input())

l = list(map(int, input().split()))

l2 = []
for i in range(n):
    x = 0
    for j in range(7):
        x += l.pop(0)
    l2.append(x)

print(*l2)