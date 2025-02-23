n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(l)

now_l = 0
time_now = 0
for i in range(n):
    x = l[i][0] - time_now
    if now_l - x >= 1:
        now_l -= x
    else:
        now_l = 0
    now_l += l[i][1]
    time_now = l[i][0]

print(now_l)
