l1, r1, l2, r2 = map(int, input().split())

l = [i for i in range(l1, r1 + 1)]
r = [i for i in range(l2, r2 + 1)]

# print(l)
# print(r)

s = set(l) & set(r)
print(len(s)-1 if len(s)-1 >= 0 else 0)