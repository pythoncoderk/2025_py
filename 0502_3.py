x, y = input().split()
s = input()

s = s.replace(x, "*")
s = s.replace(y, "@")

ans = ""
count = 0
flag = 0
for i in s:
    if i == "*":
        flag = 1
    if flag == 1:
        ans += i
    if i == "@":
        if len(ans) != 2:
            print(ans[1:-1])
            ans = ""
            flag = 2
            count += 1
        else:
            ans = ""

if count == 0:
    print("<blank>")
