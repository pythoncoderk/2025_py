s = input()

r = 0
m = 0

for i in range(len(s)):
    if s[i] == "R":
        r = i
    elif s[i] == "M":
        m = i

print("Yes" if r < m else "No")