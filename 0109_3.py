a, b, c, d, e = map(int, input().split())

l2 = [a, b, c, d, e]

l = []
for i in range(5):
    l.append(l2.count(l2[i]))

print("Yes" if l.count(3) == 3 and l.count(2) == 2 else "No")