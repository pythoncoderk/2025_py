n, l = map(int, input().split())

count = 0
l2 = list(map(int, input().split()))
for i in l2:
    if i >= l:
        count += 1

print(count)