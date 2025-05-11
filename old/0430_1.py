t = list(input())
u = input()

str_py = (["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"])
l = []
for i in range(len(t)):
    if t[i] == "?":
        l.append(i)
a = l[0]
b = l[1]
c = l[2]
d = l[3]
count = 0
for ii in range(len(str_py)):
    for j in range(len(str_py)):
        for k in range(len(str_py)):
            for ll in range(len(str_py)):
                t2 = t[::]
                t2[a] = str_py[ii]
                t2[b] = str_py[j]
                t2[c] = str_py[k]
                t2[d] = str_py[ll]
                ans = "".join(t2)
                if u in ans:
                    count += 1
print("Yes" if count >= 1 else "No")

