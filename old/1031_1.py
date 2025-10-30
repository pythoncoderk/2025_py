n = int(input())
l = list(map(str, input().split()))

s = ""
for i in range(n):
    s += l[i]

s2 = ""
for i in s:
    if i == "p" or i == "a" or i == "i" or i == "z":
        s2 += i
print(s2)
s3 = ""
x = 0
ans = ""
while True:
    if s2[x] == "p":
        ans += s2[x]
        x += 1
    if s2[x] == "a":
        ans += s2[x]
        x += 1
    if s2[x] == "i":
        ans += s2[x]
        x += 1
    if s2[x] == "z":
        ans += s2[x]
        x += 1
    if s2[x] == "a":
        ans += s2[x]
        x += 1
    s3 += s2[x]
    x += 1
