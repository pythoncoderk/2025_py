s = input()

chk = None

for i in s:
    if s.count(i) == 1:
        chk = i

for i in range(len(s)):
    if chk == s[i]:
        print(i + 1)
        break
