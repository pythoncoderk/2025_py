x, y = map(int, input().split())
xx = x + y
if xx >= 13:
    print(xx - 12)
else:
    print(xx)