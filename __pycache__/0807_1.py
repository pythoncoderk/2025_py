n, l, r = map(int, input().split())
count = 0
for i in range(n):
    x, y = map(int, input().split())
    if x <= l and y >= r:
        count += 1
print(count)