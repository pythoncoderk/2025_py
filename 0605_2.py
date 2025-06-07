l = list(map(int, input().split()))

min_l = min(l)
max_l = max(l)

total = 0

for i in l:
    if i != max_l and i != min_l:
        total += i

print(total)