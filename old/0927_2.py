n = int(input())

l = []
for i in range(n):
    l.append(i + 1)

l2 = list(map(int, input().split()))

# print(l)
# print(l2)

ans_l = []

for i in range(n):
    if l2[i] == -1:
        for j in range(len(l)):
            if l[j] not in l2:
                ans_l.append(l[j])
                l.pop(j)
                break
    else:
        for j in range(len(l)):
            if l[j] == l2[i]:
                ans_l.append(l[j])
                l.pop(j)
                break

if len(ans_l) == n:
    print("Yes")
    print(*ans_l)
else:
    print("No")

