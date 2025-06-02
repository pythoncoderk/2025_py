l = ["a", "b", "c", "d", "e", "f", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
s = list(input())
s = sorted(s)

for i in range(len(l)):
    if l[i] != s[i]:
        print(l[i])
        break
