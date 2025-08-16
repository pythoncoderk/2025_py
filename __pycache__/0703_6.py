from collections import deque

d = deque()

s = input()
flag = True
for i in s:
    if i == "(":
        d.append(i)
    else:
        if not d:
            flag = False
            break
        else:
            d.pop()
if len(d) >= 1:
    flag = False

print("Yes" if flag else "No")
