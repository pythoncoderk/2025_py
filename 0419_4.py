n, m = map(int, input().split())
l = [(list(map(int, input().split()))) for i in range(m)]
l2 = list(map(int, input().split()))


# print(n, m)
# print(l)
# print(l2)

for i in range(n):
    q = set(l2[:i+1])
    count = 0
    for j in range(len(l)):
        #print(q - l[j])
        if set(l[j]) - q == set():
            count += 1
    print(count)