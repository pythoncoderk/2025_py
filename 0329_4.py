n = int(input())
l = list(map(int, input().split()))

r = 1
l2 = [0] * n

count = 1
while n > l.count(-1):
    cc = 0
    max_l = max(l)
    for i in range(n):
        if max_l == l[i]:
            l2[i] = count
            l[i] = -1
            cc += 1
    count += cc

for i in l2:
    print(i)
