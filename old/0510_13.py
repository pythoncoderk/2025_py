n, m = map(int, input().split())
l = list(map(int, input().split()))
count = 0
while True:
    l2 = l[::]
    l3 = set(l2)
    if len(l3) == m:
        l.pop()
        count += 1
    else:
        print(count)
        exit()

