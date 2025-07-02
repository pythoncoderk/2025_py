import re

s1, s2 = map(str, input().split())
s = input()

l = []

s = re.sub(s1, "$", s)
s = re.sub(s2, "?", s)

flag = False
names = ""
for i in range(len(s)):
    if s[i] == "$":
        flag = True
    if s[i] == "?":
        flag = False
        l.append(names[1:])
        names = ""
    if flag:
        names += s[i]
if len(l) == l.count(""):
    print("<blank>")
    exit()

for i in l:
    print(i)