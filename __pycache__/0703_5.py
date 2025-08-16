from collections import deque

d = deque()

s = input()

for i in s:
    if i == "(":
        d.append(i)
    else:
        if not d:
            print("No")
            exit()
        else:
            d.pop()

print("Yes")