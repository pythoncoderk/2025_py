l = list(map(int, input().split()))
s = list(input())

for i in range(l[1]):
    s[i] = "*"

for i in range(len(s)-1, l[0]-l[2]-1, -1):
    s[i] = "*"

ans = "".join(s)
print(ans.replace("*", ""))
