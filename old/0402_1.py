n = int(input())
l = list(map(int, input().split()))

l2 = [0] * n

count = 1
for i in range(n):
    chk = 0
    max_l = max(l)
    if max_l == -1:
        break
    for j in range(n):
        if l[j] == max_l:
            l2[j] = count
            l[j] = -1
            chk += 1
    count += chk

for i in l2:
    print(i)
