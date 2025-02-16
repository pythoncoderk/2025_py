n, l, r = map(int, input().split())

l2 = [i for i in range(1, n + 1)]

print(*(l2[:l - 1] + sorted(l2[l - 1:r], reverse=True) + l2[r:]))