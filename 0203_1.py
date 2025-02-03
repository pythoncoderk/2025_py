s = input()

flag = True
for i in range(len(s)):
    if i % 2 != 0:
        if s[i] != 0:
            flag = False

print("Yes" if flag else "No")
