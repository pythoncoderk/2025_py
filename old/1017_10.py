l = input().split()
l2 = []
for i in l:
    if i not in l2:
        l2.append(i)
        print(i)
    else:
        print(1)