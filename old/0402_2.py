l = list(map(int, input().split()))

l2 = [l.count(l[i]) for i in range(len(l))]

if 2 in l2 and 3 in l2:
    print("Yes")
elif l2.count(3) >= 6:
    print("Yes")
elif 3 in l2 and 4 in l2:
    print("Yes")
elif 4 in l2 and 2 in l2:
    print("Yes")
elif 2 in l2 and 5 in l2:
    print("Yes")
else:
    print("No")