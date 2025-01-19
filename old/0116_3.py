n = int(input())
l = list(map(int, input().split()))

count = 0
max_l = max(l)
for i in range(len(l)):
    if max_l == l[i]:
        count = i

print(count + 1)