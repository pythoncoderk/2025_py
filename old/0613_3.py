n = int(input())
a, b = map(int, input().split())
l = []
for i in range(n):
    x, y = map(int, input().split())
    l.append([x, y])
l2 = sorted(l, key=lambda x: x[1])
l2 = sorted(l2, key=lambda x: x[0])

print(n)
print(a, b)
print(l)
print(l2)

ans1 = 0
flag = True
for i in range(n):
    if l2[i][0] > a:
        ans1 = i+1
        flag = False
        break
    if l2[i][0] == a:
        if l2[i][1] > b:
            ans1 = i+1
            flag = False
            break
print(n + 1 if flag else ans1)

l3 = []
for i in range(n):
    if l[i][0] == 4 and 2 <= l[i][1] >= 30:
        l[i][0] -= 4
        if l[i][0] < 0:
            l[i][0] += 12
    else:
        l[i][0] = 13

    if l[i][0] != 4:
        l[i][0] -= 4
        if l[i][0] < 0:
            l[i][0] += 12
    l3.append(l[i])

l3 = sorted(l, key=lambda x: x[1])
l3 = sorted(l2, key=lambda x: x[0])
print(l3)

a -= 4
if a < 0:
    a += 12

ans2 = 0
flag = True
for i in range(n):
    if l3[i][0] > a:
        ans2 = i+1
        flag = False
        break
    if l3[i][0] == a:
        if l[i][1] > b:
            ans2 = i+1
            flag = False
            break
print(n + 1 if flag else ans2)




