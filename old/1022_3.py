a, b = map(str, input().split())
s = input()

star = 0

while True:
    x = s[star:]
    print(f"{x.find(a)+1 + star} {x.find(b)+1 + star}")
    star = s.find(b)+1 + len(b)