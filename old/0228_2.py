n, m = map(int, input().split())
x = int(input())
l = list(map(int, input().split()))
l2 = [i for i in l if i % n == 0]

for i in range(m):
    orange = int(input())
    g = None
    ans = None
    for j in l2:
        if g is None:
            g = abs(orange - j)
            ans = j
        else:
            if g >= abs(orange - j):
                g = abs(orange - j)
                ans = j
    print(ans)
