n = int(input())

s = input()
t = input()

flag = []
for i in range(n):
    if s[i] == "1" or s[i] == "l":
        if t[i] == "1" or t[i] == "l":
            flag.append(0)
        else:
            flag.append(1)
    elif s[i] == "0" or s[i] == "o":
        if t[i] == "o" or t[i] == "0":
            flag.append(0)
        else:
            flag.append(1)
    else:
        if s[i] == t[i]:
            flag.append(0)
        else:
            flag.append(1)

print("Yes" if max(flag) == 0 else "No")