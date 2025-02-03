n, x = map(int, input().split())

l = list(map(int, input().split()))

total = 0
for i in l:
    if i <= x:
        total += i
print(total)