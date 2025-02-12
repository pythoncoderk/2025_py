a, b, c = map(int, input().split())

l = []
while True:
    if b == c:
        break
    else:
        l.append(b)
        b += 1
    if b == 24:
        b = 0

print("Yes" if a not in l else "No")