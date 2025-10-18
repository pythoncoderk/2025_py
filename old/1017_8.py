l = input().split()

l2 = []
for i in l:
    if i in l2:
        print("already_been")
    else:
        l2.append(i)
        print(i)