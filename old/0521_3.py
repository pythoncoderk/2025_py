n, k = map(int, input().split())
l = list(map(int, input().split()))


def ans(arr):
    new_l = []
    count = 1
    while True:
        x = arr.pop(0)
        if not arr:
            new_l.append(x)
            new_l.append(count)
            break
        if arr[0] == x:
            count += 1
        else:
            new_l.append(x)
            new_l.append(count)
            count = 1
    return new_l

x = l[::]
for i in range(k):
   x = ans(x)

print(*x)