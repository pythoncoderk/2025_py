import itertools

n = input()

l = []
for i in range(len(n)):
    l.append(n[i])
l2 = []
for i in l:
    l2.append(int(i))

l3 = []
for i in itertools.permutations(l2, len(l2)):
    l3.append(i)

l4 = sorted(l3)

for i in l4:
    if i[0] != 0:
        for j in range(len(i)):
            print(i[j], end='')
        exit()
