n = int(input())

count = 0
bit = 1
while bit <= n:
    if bit & n != 0:
        count += 1
    bit *= 2

print(count)