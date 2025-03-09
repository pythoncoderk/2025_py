n = int(input())

l = [input() for i in range(n)]
l2 = [[len(l[i]), l[i]] for i in range(n)]

l2.sort()

ans = ""
for i in range(n):
    ans += l2[i][1]

print(ans)