l = list(map(int, input().split()))
s = list(map(str, input().split()))

total = 0
for i in range(len(l)):
    if s[i] == "o":
        total += l[i]

print(int((total / sum(l)) * 100))