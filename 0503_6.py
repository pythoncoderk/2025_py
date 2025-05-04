import copy

n = int(input())

s = []
for i in range(n):
    l = list(input())
    s.append(l)

t = []
for i in range(n):
    l = list(input())
    t.append(l)

l2 = copy.deepcopy(s)

print(s)
print(t)
# print(l2)
ans = 1
count1 = 0
for i in range(n):
    for j in range(n):
        if l2[i][j] != t[i][j]:
            count1 += 1
if count1 == 1:
    print(0)
    exit()
count2 = 0
while count2 != 1:
    x = n - 1
    for jj in range(n):
        for k in range(n):
            l2[k][x] = s[jj][k]
        x -= 1
    count2 = 0
    for xx in range(n):
        for yy in range(n):
            if l2[xx][yy] != t[xx][yy]:
                count2 += 1
    ans += 1

print(ans)


