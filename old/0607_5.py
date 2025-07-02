n = int(input())
l = list(map(int, input().split()))

max_l = 0
max_count = 0

for i in range(n+1):
    count = 0
    for j in range(n):
        if i <= l[j]:
            count += 1
    if count >= i:
        max_count = count
        max_l = i
print(max_l)

