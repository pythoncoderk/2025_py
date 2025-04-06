h, a = map(int, input().split())

x = h // a
y = h % a

print(x if y == 0 else x + 1)