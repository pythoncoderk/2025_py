
s = input()

for i in range((len(s) - 3) * 2):
    name = ""
    for j in range(i, len(s)):
        name += s[j]
        if len(name) == 3:
            break