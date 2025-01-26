n = int(input())

s = input()

t = 0
a = 0

for i in range(len(s)):
    if s[i] == "T":
        t += 1
    else:
        a += 1

if t == a:
    if s[-1] == "T":
        print("A")
    else:
        print("T")
elif t > a:
    print("T")
else:
    print("A")

