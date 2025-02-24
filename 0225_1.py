l = list(map(str, input().split()))

l2 = []
for i in l:
    if i in l2:
        print("already_been")
    else:
        print(i)
        l2.append(i)
