h, w, n = map(int, input().split())
l = [list(map(str, input().split())) for i in range(h * n)]
r, c = map(int, input().split())
l2 = [list(map(int, input().split())) for i in range(r)]

x = l[0]
y = l[1]
print(x)
print(y)