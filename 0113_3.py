def gcb(a, b):
    if b == 0:
        return a
    return gcb(b, a % b)

a, b = map(int, input().split())
print(gcb(a, b))