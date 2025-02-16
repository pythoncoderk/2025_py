l = list(map(str, input().split()))

l_allredy = []

for i in range(len(l)):
    if l[i] in l_allredy:
        print("already_been")
    else:
        print(l[i])
        l_allredy.append(l[i])