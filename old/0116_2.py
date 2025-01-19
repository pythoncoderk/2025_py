from decimal import Decimal, ROUND_HALF_UP

a, b = map(int, input().split())

x = b / a

print(Decimal(str(x)).quantize(Decimal("0.001"), ROUND_HALF_UP))


