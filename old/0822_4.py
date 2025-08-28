a, b = map(str, input().split())
s = input()

p = 0

while True:
    x = s[p::].find(a)
    p += 1