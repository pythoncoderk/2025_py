a, b = map(str,input().split())
s = input()

n = 0
while n < len(s):
    s = s[n:]
    print(f"{s.find(a)+1+n} {s.find(b)+1+n}")
    n += s.find(b)+1+len(b)