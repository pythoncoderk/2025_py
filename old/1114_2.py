a, b, c = map(int, input().split())
l = [a, b, c]

x = sorted(l)

print(x[-1], end='')
print(x[-2], end='')
print(x[-3], end='')
