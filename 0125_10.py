n = int(input())

l = list(map(int, input().split()))


ans = []
for i in range(len(l)-1):
    ans.append(float(l[i+1] / l[i]))


print("Yes" if ans.count(ans[0]) == len(ans) else "No")