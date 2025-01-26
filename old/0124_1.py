n = int(input())

l = [list(map(str, input().split())) for i in range(n)]

min_l = 999999999999999999999999999999999999
index_l = 0
for i in range(n):
    if int(l[i][1]) < min_l:
        min_l = int(l[i][1])
        index_l = i

ans_l = l[index_l:] + l[:index_l]

for i in range(n):
    print(ans_l[i][0])