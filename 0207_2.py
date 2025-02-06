s = input()

flag = True

if s[0].islower():
    flag = False

for i in range(len(s)):
    if i != 0:
        if s[i].isupper():
            flag = False

print("Yes" if flag else "No")