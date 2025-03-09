n, m = map(str, input().split())
s = input()

s = s.replace(n, "*")
s = s.replace(m, "@")
count = 0
for i in range(len(s)):
    ans = ""
    if s[i] == "*":
        for j in range(i+1, len(s)):
            if s[j] == "@":
                if ans != "":
                    print(ans)
                    count += 1
                    break
            else:
                if s[j] != "*" or s[j] != "@":
                    ans += s[j]

if count == 0:
    print("<blank>")
