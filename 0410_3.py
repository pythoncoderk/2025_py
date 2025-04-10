n = int(input())
l = list(map(str, input().split()))

count = 0
l2 = []
for i in range(n):
    l3 = []
    for j in range(n):
        if l[i] == "C" and l[j] == "R":
            l3.append(i + 1)
            l3.append(j + 1)
            count += 1
            l[j] = "X"
            break
    l2.append(l3)


if count == 0:
    print(0)
else:
    print(count)

for i in range(len(l2)):
    if l2[i] != []:
        print(*l2[i])
