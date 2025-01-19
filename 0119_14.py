n = int(input())
a = [int(x) for x in input().split()]

maximum = -100
minimum = 100
for value in a:
    if value > maximum:
        maximum = value

    if value < minimum:
        minimum = value

print(maximum, minimum)
