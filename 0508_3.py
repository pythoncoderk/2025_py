s = input()

for i in range(1 << len(s) - 1):
    l = []
    for j in range(len(s) - 1):
        if i & (1 << j):
            l.append("o")
        else:
            l.append("x")
    ans = ""
    total = 0
    for x in range(len(s)):
        if x == 0:
            ans += s[x]
        else:
            if l[x] == "o":
                total += int(ans)
                ans = ""
