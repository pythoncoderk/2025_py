a, b = map(int, input().split())

one = [1]
two = [2]
tree = [1, 2]
foer = [4]
five = [1, 4]
six = [2, 4]
seven = [1, 2, 4]

total = []
if a == 1: total += one
elif a == 2: total += two
elif a == 3: total += tree
elif a == 4: total += foer
elif a == 5: total += five
elif a == 6: total += six
elif a == 7: total += seven

if b == 1: total += one
elif b == 2: total += two
elif b == 3: total += tree
elif b == 4: total += foer
elif b == 5: total += five
elif b == 6: total += six
elif b == 7: total += seven

print(sum(set(total)))

