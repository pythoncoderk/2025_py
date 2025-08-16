s = input()
t = input()

l = [t[i] for i in range(len(t))]

l2 = []

for i in range(len(s)):
    if s[i].isupper() and i != 0:
        l2.append(s[i-1])
ans = True
for i in range(len(l2)):
    if l2[i] not in l:
        ans = False
print("Yes" if ans else "No")

