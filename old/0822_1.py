import re

a, b = map(str, input().split())
s = input()

s2 = re.sub(a, "*", s)
s2 = re.sub(b, "@", s2)
flag = False
count = 0
for i in s2:
    if flag and i != "@":
        print(i, end="")
        count += 1

    if i == "*":
        flag = True
    elif i == "@":
        flag = False
        print()

if count == 0:
    print("<blank>")




