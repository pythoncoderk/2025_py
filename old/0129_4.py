n = int(input())
s = input()

abc = []
for i in range(n):
    if s[i] not in abc:
        abc.append(s[i])
    if len(abc) == 3:
        print(i + 1)
        break
