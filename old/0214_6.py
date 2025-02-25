n = int(input())
s = input()

count = 0
for i in range(n - 3 + 1):
    if s[i] == "#" and s[i + 1] == "." and s[i + 2] == "#":
        count += 1

print(count)