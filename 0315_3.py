s = list(input())


i = 0
count = 0
while len(s) > i:
    if i % 2 == 0:
        if s[i] != "i":
            s.insert(i, "i")
            count += 1
    else:
        if s[i] != "o":
            s.insert(i, "o")
            count += 1
    i += 1

print(count if len(s) % 2 == 0 else count + 1)