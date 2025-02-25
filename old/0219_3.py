n, c = map(int, input().split())
l = list(map(int, input().split()))

# print(n, c)
# print(l)

count = 0
x = 0
for i in range(len(l)):
    if i == 0:
        count += 1
        x = l[i]
    elif l[i] - x >= c:
        count += 1
        x = l[i]
print(count)

