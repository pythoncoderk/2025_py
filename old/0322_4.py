l = list(map(int, input().split()))

l2 = []
for i in l:
    l2.append(l.count(i))

if (
        (2 in l2 and 3 in l2)
        or (2 in l2 and 4 in l2)
        or (2 in l2 and 5 in l2)
        or (4 in l2 and 2 in l2)
        or (4 in l2 and 3 in l2)
):
    print("Yes")
else:
    print("No")