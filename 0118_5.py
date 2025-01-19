n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(l)

ans = []
last = 0
for i in range(n):
    if l[i][0] == 1:
        if len(ans) == 0:
            ans.append(0)
            last = l[i][1]
        else:
            ans.append(last)
            last += l[i][1]
    elif l[i][0] == 2:
        if len(ans) >= 2:
            main = ans[1] - ans[0]
            ans.pop(0)
            for j in range(len(ans)):
                ans[j] -= main
            last = l[i-1][1] + ans[-1]
    else:
        print(ans[l[i][1] - 1])

