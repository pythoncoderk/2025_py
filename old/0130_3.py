n, h, x = map(int, input().split())
l = list(map(int, input().split()))

l2 = [h + l[i] for i in range(n)]

ans_min = 100000000000000000000000000000000
ans_index = 0
for i in range(n):
    if ans_min > l2[i] >= x:
        ans_min = l2[i]
        ans_index = i

print(ans_index + 1)