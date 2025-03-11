import re

n, m = map(str, input().split())
s = input()

x = re.findall("<abc>.?<xyz>", s)
print(x)