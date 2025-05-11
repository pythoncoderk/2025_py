s = input()
total = 0

for i in range(1 << len(s)-1):
    l = []
    ans = s[0]
    for j in range(len(s)-1):
        if i & (1 << j):
            l.append("+")
        else:
            l.append("")
    for z in range(len(l)):
        if l[z] == "+":
            total += int(ans)
            ans = s[0]
        else:
            ans += s[z+1]
    total += int(ans)
    ans = s[0]