n, m = map(int, input().split())

l = []
for i in range(n):
    l2 = [0] * n
    x = input()
    for j in range(n):
        l2[j] = x[j]
    l.append(l2)

print(l)

ans_l = []
for i in range(n * (n - 1)):
    l3 = []
    for j in range(n-m+1):
        for k in range(n-m+1):
            l3.append(l[k][j])
    ans_l.append(l3)

print(ans_l)
print(len(ans_l))



