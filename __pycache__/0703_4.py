s = input()

m = 0
n = 0

for i in s:
    if i == "(":
        m += 1
    else:
        n += 1

print("Yes" if m == n else "No")