s = input()

flag = False
if s[0] == "<":
    if s[-1] == ">":
        for i in range(1, len(s)-1):
            if s[i] == "=":
                flag = True
            else:
                flag = False
                break

print("Yes" if flag else "No")