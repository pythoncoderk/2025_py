s = input()

count = 0
for i in range(len(s)):
    if s[i] == ".":
        count = i

print(s[count + 1:])