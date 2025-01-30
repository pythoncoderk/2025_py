n, d = map(int, input().split())
al = list(map(int, input().split()))
xl = list(map(int, input().split()))

total_l = []
for i in range(len(al)):
    if i == 0:
        total_l.append(al[i])
    else:
        total_l.append(total_l[i - 1] + al[i])


ans = 0
for i in range(len(xl)):
    for j in range(len(total_l)):
        if xl[i] <= total_l[j]:
            if xl[i] == total_l[j]:
                ans += j + 1
            else:
                ans += j
            break
        else:
            if j + 1 == len(total_l):
                ans += j + 1
print(ans)