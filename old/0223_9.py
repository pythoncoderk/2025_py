l = list(map(int, input().split()))

a = l.count(l[0])
b = l.count(l[1])
c = l.count(l[2])
d = l.count(l[3])

l2 = [a, b, c, d]

if l2.count(3) == 3 and l2.count(1) == 1:
    print("Yes")
elif l2.count(2) == 4:
    print("Yes")
else:
    print("No")

