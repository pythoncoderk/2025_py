a, b = map(str, input().split())
s = input()

s = s.replace(a, "*")
s = s.replace(b, "#")
count = 0
flag = True
for i in range(len(s)):
    if s[i] == "*":
        flag = False
    if not flag:
        st = i + 1
        ans = ""
        while True:
            if s[st] == "#":

                break
            else:
                ans += s[st]
                st += 1
        if ans != "":
            print(ans)
            count += 1

        flag = True

if count == 0:
    print("<blank>")