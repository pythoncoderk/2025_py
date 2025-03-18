n, m = map(int, input().split())

x = n // m
y = n % m

print(x + 1 if y != 0 else x)