a, b = map(int, input().split())

l = [a, b]
count = 0
for i in range(-200, 200):
    l.append(i)
    l.sort()
    if l[1] - l[0] == l[2] - l[1]:
        count += 1
    l = [a, b]

print(count)
