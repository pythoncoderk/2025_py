from decimal import *

a, b = map(int, input().split())

x = float(a / b)
ans = Decimal(str(x)).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
print(ans)