import re

s1 = input()
s2 = input()

x = s1.find("?")
f_str = s1[x:]

flag = True
for i in range(len(s2)):
    if s2[i] == f_str[i] or f_str[i] == "?":
        pass
    else:
        flag = False

print("Yes" if flag else "No")