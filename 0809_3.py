from decimal import Decimal, ROUND_HALF_UP
from collections import deque

s = list(input())
d = deque(s)

while len(d) != 0:
    if d[0] != "t":
        d.popleft()
    else:
        break

while len(d) != 0:
    if d[-1] != "t":
        d.pop()
    else:
        break

if d.count("t") <= 2:
    print(0)
    exit()

x = d.count("t") - 2
t = (len(d)) - 2


print(Decimal(x / t))
