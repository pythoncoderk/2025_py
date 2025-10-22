a, b = map(str,input().split())
s = input()
n = 0
while True:
    x = s[n:]
    if x == "":
        break
    if x.find(a) == x.find(b):
        break
    print(f"{x.find(a)+1 + n} {x.find(b)+1 + n}")
    n = x.find(b)+1+n + len(b)