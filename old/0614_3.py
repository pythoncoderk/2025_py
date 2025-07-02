from decimal import *

a = int(input())
b = int(input())
c = int(input())

print(max(a, b, c))
print(sum([a, b, c, d, e, f, g])/7)
ans = Decimal(str(sum([a, b, c, d, e, f, g])/7)).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
print(ans)
print(int(ans))

n = int(input())
l = list(map(int, input().split()))
print(max(l), min(l))
print(min(l), max(l))