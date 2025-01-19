h, w = map(int, input().split())
r, c = map(int, input().split())

l = []
for i in range(1, h + 1):
    for j in range(1, w + 1):
        l.append([i, j])

count = 0
if [r - 1, c] in l:
    count += 1

if [r + 1, c] in l:
    count += 1

if [r, c - 1] in l:
    count += 1

if [r, c + 1] in l:
    count += 1

print(count)

