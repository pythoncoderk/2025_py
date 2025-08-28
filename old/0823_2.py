from itertools import count

n, m = map(int, input().split())
l = []
l_ans = []
for i in range(n):
    l.append(input())

for i in range(m):
    l2 = []
    for j in range(n):
        l2.append(l[j][i])
    l_ans.append(l2)

f_l = [0] * n

for i in range(m):
    one = l_ans[i].count('1')
    zero = l_ans[i].count('0')

    if zero == 0 or one == 0:
        for j in range(n):
            f_l[j] += 1
    elif one > zero:
        for j in range(n):
            if l_ans[i][j] == '0':
                f_l[j] += 1
    else:
        for j in range(n):
            if l_ans[i][j] == '1':
                f_l[j] += 1
maxl = max(f_l)

for i in range(n):
    if maxl == f_l[i]:
        if i != n - 1:
            print(i + 1, end=' ')
        else:
            print(i + 1)


