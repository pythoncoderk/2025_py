l = list(map(str, input().split()))

l_a = []

for i in l:
    if i not in l_a:
        print(i)
        l_a.append(i)

