n, p, q, r, s = map(int, input().split())

l = list(map(int, input().split()))

# print(l[p-1:q])
# print(l[r-1:s])

l[p-1:q], l[r-1:s] = l[r-1:s], l[p-1:q]

print(*l)