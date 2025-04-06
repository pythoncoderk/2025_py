n = int(input())
l = list(map(int, input().split()))
ans_l = [0] * n

ans_count = 0
for i in range(n):
    count = 0
    max_l = max(l)
    if max_l == -1:
        break
    for j in range(n):
        if l[j] == max_l:
            l[j] = -1
            ans_l[j] = ans_count + 1
            count += 1
    ans_count += count
for i in ans_l:
    print(i)


