n, t, a = map(int, input().split())

x = n - t - a
y = abs(t - a)

if x < y:
    print("Yes")
else:
    print("No")

