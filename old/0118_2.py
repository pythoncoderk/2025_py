n, m = map(int, input().split())

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l3 = list(map(int, input().split()))

# print(l1)
# print(l2)
# print(l3)

final = []

for i in range(n):

    for j in range(n):

        for k in range(n):
            ans_l = []
            cal = 0
            ans_total = 0
            if i != j and j != k and i != k:
                if l3[i] != l3[j] and l3[j] != l3[k] and l3[i] != l3[k]:
                    cal += l1[i] + l1[j] + l1[k]
                    ans_total += l2[i] + l2[j] + l2[k]
                    if cal <= m:
                        final.append(ans_total)
if len(final) == 0:
    print(-1)
else:
    print(max(final))